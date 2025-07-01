private static ByteBuf allocateBuffer(ByteBufAllocator allocator, byte id, int contentLength) {
		return allocateBuffer(allocator, id, 0, contentLength, true);
	}