protected void releaseTable() {
		// set the counters back
		this.numBuckets = 0;
		
		if (this.buckets != null) {
			for (MemorySegment bucket : this.buckets) {
				this.availableMemory.add(bucket);
			}
			this.buckets = null;
		}
	}