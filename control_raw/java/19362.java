private MethodHandle nullChecker(Class<?> javaType)
    {
        if (javaType == Long.class) {
            return CHECK_LONG_IS_NOT_NULL;
        }
        else if (javaType == Double.class) {
            return CHECK_DOUBLE_IS_NOT_NULL;
        }
        else if (javaType == Boolean.class) {
            return CHECK_BOOLEAN_IS_NOT_NULL;
        }
        else if (javaType == Slice.class) {
            return CHECK_SLICE_IS_NOT_NULL;
        }
        else if (javaType == Block.class) {
            return CHECK_BLOCK_IS_NOT_NULL;
        }
        else {
            throw new IllegalArgumentException("Unknown java type " + javaType);
        }
    }