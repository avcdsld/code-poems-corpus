@Override
    public DurableDataLog.ReadItem getNext() throws DurableDataLogException {
        Exceptions.checkNotClosed(this.closed.get(), this);

        if (this.currentLedger == null) {
            // First time we call this. Locate the first ledger based on the metadata truncation address. We don't know
            // how many entries are in that first ledger, so open it anyway so we can figure out.
            openNextLedger(this.metadata.getNextAddress(this.metadata.getTruncationAddress(), Long.MAX_VALUE));
        }

        while (this.currentLedger != null && (!this.currentLedger.canRead())) {
            // We have reached the end of the current ledger. Find next one, and skip over empty ledgers).
            val lastAddress = new LedgerAddress(this.currentLedger.metadata, this.currentLedger.handle.getLastAddConfirmed());
            Ledgers.close(this.currentLedger.handle);
            openNextLedger(this.metadata.getNextAddress(lastAddress, this.currentLedger.handle.getLastAddConfirmed()));
        }

        // Try to read from the current reader.
        if (this.currentLedger == null || this.currentLedger.reader == null) {
            return null;
        }

        return new LogReader.ReadItem(this.currentLedger.reader.nextElement(), this.currentLedger.metadata);
    }