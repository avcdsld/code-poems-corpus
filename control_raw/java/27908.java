private boolean handleClosedLedgers(List<Write> writes) {
        if (writes.size() == 0 || !writes.get(0).getWriteLedger().ledger.isClosed()) {
            // Nothing to do. We only need to check the first write since, if a Write failed with LedgerClosed, then the
            // first write must have failed for that reason (a Ledger is closed implies all ledgers before it are closed too).
            return false;
        }

        long traceId = LoggerHelpers.traceEnterWithContext(log, this.traceObjectId, "handleClosedLedgers", writes.size());
        WriteLedger currentLedger = getWriteLedger();
        Map<Long, Long> lastAddsConfirmed = new HashMap<>();
        boolean anythingChanged = false;
        for (Write w : writes) {
            if (w.isDone() || !w.getWriteLedger().ledger.isClosed()) {
                continue;
            }

            // Write likely failed because of LedgerClosedException. Need to check the LastAddConfirmed for each
            // involved Ledger and see if the write actually made it through or not.
            long lac = fetchLastAddConfirmed(w.getWriteLedger(), lastAddsConfirmed);
            if (w.getEntryId() >= 0 && w.getEntryId() <= lac) {
                // Write was actually successful. Complete it and move on.
                completeWrite(w);
                anythingChanged = true;
            } else if (currentLedger.ledger.getId() != w.getWriteLedger().ledger.getId()) {
                // Current ledger has changed; attempt to write to the new one.
                w.setWriteLedger(currentLedger);
                anythingChanged = true;
            }
        }

        LoggerHelpers.traceLeave(log, this.traceObjectId, "handleClosedLedgers", traceId, writes.size(), anythingChanged);
        return anythingChanged;
    }