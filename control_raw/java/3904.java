@Override
	public List<MemorySegment> close() throws IOException {
		if (this.closed) {
			throw new IllegalStateException("Already closed.");
		}
		this.closed = true;

		// re-collect all memory segments
		ArrayList<MemorySegment> list = this.freeMem;
		final MemorySegment current = getCurrentSegment();
		if (current != null) {
			list.add(current);
		}
		clear();

		// close the writer and gather all segments
		final LinkedBlockingQueue<MemorySegment> queue = this.reader.getReturnQueue();
		this.reader.close();

		while (list.size() < this.numSegments) {
			final MemorySegment m = queue.poll();
			if (m == null) {
				// we get null if the queue is empty. that should not be the case if the reader was properly closed.
				throw new RuntimeException("Bug in ChannelReaderInputView: MemorySegments lost.");
			}
			list.add(m);
		}
		return list;
	}