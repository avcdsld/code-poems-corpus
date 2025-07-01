@SneakyThrows
    private static <T> T readObjectByReflection(final Kryo kryo, final Input input, final Class<T> clazz) {
        val className = kryo.readObject(input, String.class);
        val foundClass = (Class<T>) Class.forName(className);
        val result = kryo.readObject(input, foundClass);

        if (!clazz.isAssignableFrom(result.getClass())) {
            throw new ClassCastException("Result [" + result
                + " is of type " + result.getClass()
                + " when we were expecting " + clazz);
        }
        return result;
    }