public RESP deserializeResponse(final ByteBuf buf) {
		Preconditions.checkNotNull(buf);
		return responseDeserializer.deserializeMessage(buf);
	}