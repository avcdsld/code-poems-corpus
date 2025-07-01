public List<MemorySegment> allocatePages(Object owner, int numPages) throws MemoryAllocationException {
		final ArrayList<MemorySegment> segs = new ArrayList<MemorySegment>(numPages);
		allocatePages(owner, segs, numPages);
		return segs;
	}