@Override
	public void open() {
		synchronized (stateLock) {
			if (!closed) {
				throw new IllegalStateException("currently not closed.");
			}
			closed = false;
		}
		
		// create the partitions
		final int partitionFanOut = getPartitioningFanOutNoEstimates(this.availableMemory.size()); 
		createPartitions(partitionFanOut);
		
		// set up the table structure. the write behind buffers are taken away, as are one buffer per partition
		final int numBuckets = getInitialTableSize(this.availableMemory.size(), this.segmentSize, 
			partitionFanOut, this.avgRecordLen);
		
		initTable(numBuckets, (byte) partitionFanOut);
	}