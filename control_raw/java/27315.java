synchronized QueueStats getStatistics() {
        int size = this.writes.size();
        double fillRatio = calculateFillRatio(this.totalLength, size);
        int processingTime = this.lastDurationMillis;
        if (processingTime == 0 && size > 0) {
            // We get in here when this method is invoked prior to any operation being completed. Since lastDurationMillis
            // is only set when an item is completed, in this special case we just estimate based on the amount of time
            // the first item in the queue has been added.
            processingTime = (int) ((this.timeSupplier.get() - this.writes.peekFirst().getQueueAddedTimestamp()) / AbstractTimer.NANOS_TO_MILLIS);
        }

        return new QueueStats(size, fillRatio, processingTime);
    }