public TarEntry getNextEntry() throws IOException {
        if (this.hasHitEOF) {
            return null;
        }

        if (this.currEntry != null) {
            long numToSkip = this.entrySize - this.entryOffset;

            if (this.debug) {
                System.err.println("TarInputStream: SKIP currENTRY '"
                        + this.currEntry.getName() + "' SZ "
                        + this.entrySize + " OFF "
                        + this.entryOffset + "  skipping "
                        + numToSkip + " bytes");
            }

            if (numToSkip > 0) {
                this.skip(numToSkip);
            }

            this.readBuf = null;
        }

        byte[] headerBuf = this.buffer.readRecord();

        if (headerBuf == null) {
            if (this.debug) {
                System.err.println("READ NULL RECORD");
            }
            this.hasHitEOF = true;
        } else if (this.buffer.isEOFRecord(headerBuf)) {
            if (this.debug) {
                System.err.println("READ EOF RECORD");
            }
            this.hasHitEOF = true;
        }

        if (this.hasHitEOF) {
            this.currEntry = null;
        } else {
            this.currEntry = new TarEntry(headerBuf);

            if (this.debug) {
                System.err.println("TarInputStream: SET currENTRY '"
                        + this.currEntry.getName()
                        + "' size = "
                        + this.currEntry.getSize());
            }

            this.entryOffset = 0;

            this.entrySize = this.currEntry.getSize();
        }

        if (this.currEntry != null && this.currEntry.isGNULongNameEntry()) {
            // read in the name
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            byte[] buf = new byte[256];
            int length;
            while ((length = read(buf)) >= 0) {
                baos.write(buf,0,length);
            }
            getNextEntry();
            if (this.currEntry == null) {
                // Bugzilla: 40334
                // Malformed tar file - long entry name not followed by entry
                return null;
            }
            String longName = baos.toString("UTF-8");
            // remove trailing null terminator
            if (longName.length() > 0
                && longName.charAt(longName.length() - 1) == 0) {
                longName = longName.substring(0,longName.length()-1);
            }
            this.currEntry.setName(longName);
        }

        return this.currEntry;
    }