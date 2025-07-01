public static String deflate(final byte[] bytes) {
        val data = new String(bytes, StandardCharsets.UTF_8);
        return deflate(data);
    }