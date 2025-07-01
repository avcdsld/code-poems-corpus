function(dbaseFile, buffer, recordNumber) {
            if (!dbaseFile) {
                throw new ArgumentError(
                    Logger.logMessage(Logger.LEVEL_SEVERE, "DBaseRecord", "constructor", "missingAttributeName")
                );
            }

            if (!buffer) {
                throw new ArgumentError(
                    Logger.logMessage(Logger.LEVEL_SEVERE, "DBaseRecord", "constructor", "missingBuffer")
                );
            }

            /**
             * Indicates whether the record was deleted.
             * @type {Boolean}
             */
            this.deleted = false;

            /**
             * Indicates the current record number.
             * @type {Number}
             */
            this.recordNumber = recordNumber;

            //DateFormat dateformat = new SimpleDateFormat("yyyyMMdd");

            this.values = null;

            this.readFromBuffer(dbaseFile, buffer, recordNumber);
        }