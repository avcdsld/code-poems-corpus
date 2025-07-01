@Override
	public SerializationResult copyToBufferBuilder(BufferBuilder targetBuffer) {
		targetBuffer.append(lengthBuffer);
		targetBuffer.append(dataBuffer);
		targetBuffer.commit();

		return getSerializationResult(targetBuffer);
	}