public final void copyTo(int offset, MemorySegment target, int targetOffset, int numBytes) {
		final byte[] thisHeapRef = this.heapMemory;
		final byte[] otherHeapRef = target.heapMemory;
		final long thisPointer = this.address + offset;
		final long otherPointer = target.address + targetOffset;

		if ((numBytes | offset | targetOffset) >= 0 &&
				thisPointer <= this.addressLimit - numBytes && otherPointer <= target.addressLimit - numBytes) {
			UNSAFE.copyMemory(thisHeapRef, thisPointer, otherHeapRef, otherPointer, numBytes);
		}
		else if (this.address > this.addressLimit) {
			throw new IllegalStateException("this memory segment has been freed.");
		}
		else if (target.address > target.addressLimit) {
			throw new IllegalStateException("target memory segment has been freed.");
		}
		else {
			throw new IndexOutOfBoundsException(
					String.format("offset=%d, targetOffset=%d, numBytes=%d, address=%d, targetAddress=%d",
					offset, targetOffset, numBytes, this.address, target.address));
		}
	}