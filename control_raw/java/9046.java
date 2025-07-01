public static Object mergeObject(Object config, Class clazz) {
        merge(config);
        return convertMapToObj((Map<String, Object>) config, clazz);
    }