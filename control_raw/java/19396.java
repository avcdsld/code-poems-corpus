public T fromSmile(byte[] bytes)
            throws IllegalArgumentException
    {
        try {
            return mapper.readValue(bytes, javaType);
        }
        catch (IOException e) {
            throw new IllegalArgumentException(format("Invalid SMILE bytes for %s", javaType), e);
        }
    }