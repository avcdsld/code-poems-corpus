@Override
    public T deserialize(String json) {
        ObjectMapper mapper = SequenceElement.mapper();
        try {
            T ret = (T) mapper.readValue(json, targetClass);
            return ret;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }