SegmentChunk withNewOffset(long newOffset) {
        SegmentChunk ns = new SegmentChunk(this.name, newOffset);
        ns.setLength(getLength());
        if (isSealed()) {
            ns.markSealed();
        }

        if (!exists()) {
            ns.markInexistent();
        }

        return ns;
    }