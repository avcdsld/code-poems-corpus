public DataBuffer decompress(DataBuffer buffer, DataType targetType) {
        if (buffer.dataType() != DataType.COMPRESSED)
            throw new IllegalStateException("You can't decompress DataBuffer with dataType of: " + buffer.dataType());

        CompressedDataBuffer comp = (CompressedDataBuffer) buffer;
        CompressionDescriptor descriptor = comp.getCompressionDescriptor();

        if (!codecs.containsKey(descriptor.getCompressionAlgorithm()))
            throw new RuntimeException("Non-existent compression algorithm requested: ["
                            + descriptor.getCompressionAlgorithm() + "]");

        return codecs.get(descriptor.getCompressionAlgorithm()).decompress(buffer, targetType);
    }