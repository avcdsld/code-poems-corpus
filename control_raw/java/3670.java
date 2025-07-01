public static ByteBuf serializeServerFailure(
			final ByteBufAllocator alloc,
			final Throwable cause) throws IOException {

		final ByteBuf buf = alloc.ioBuffer();

		// Frame length is set at end
		buf.writeInt(0);
		writeHeader(buf, MessageType.SERVER_FAILURE);

		try (ByteBufOutputStream bbos = new ByteBufOutputStream(buf);
				ObjectOutput out = new ObjectOutputStream(bbos)) {
			out.writeObject(cause);
		}

		// Set frame length
		int frameLength = buf.readableBytes() - Integer.BYTES;
		buf.setInt(0, frameLength);
		return buf;
	}