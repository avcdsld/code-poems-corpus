public static <T> T getDefaultWrapperValue(Class<T> clazz) {
        if (clazz == Short.class) {
            return (T) Short.valueOf((short) 0);
        } else if (clazz == Integer.class) {
            return (T) Integer.valueOf(0);
        } else if (clazz == Long.class) {
            return (T) Long.valueOf(0L);
        } else if (clazz == Double.class) {
            return (T) Double.valueOf(0d);
        } else if (clazz == Float.class) {
            return (T) Float.valueOf(0f);
        } else if (clazz == Byte.class) {
            return (T) Byte.valueOf((byte) 0);
        } else if (clazz == Character.class) {
            return (T) Character.valueOf((char) 0);
        } else if (clazz == Boolean.class) {
            return (T) Boolean.FALSE;
        }
        return null;
    }