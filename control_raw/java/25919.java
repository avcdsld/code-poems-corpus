byte[] writeAndClose(byte[] payload, StreamWrapper wrapper) throws IOException {
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream(512);
        OutputStream compressionStream = wrapper.wrap(outputStream);
        try {
            compressionStream.write(payload);
            compressionStream.flush();
        } finally {
            Objects.nullSafeClose(compressionStream);
        }
        return outputStream.toByteArray();
    }