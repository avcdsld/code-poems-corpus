public static long offset(long[] strides, long[] offsets) {
        int ret = 0;

        if (ArrayUtil.prod(offsets) == 1) {
            for (int i = 0; i < offsets.length; i++) {
                ret += offsets[i] * strides[i];
            }
        } else {
            for (int i = 0; i < offsets.length; i++) {
                ret += offsets[i] * strides[i];
            }

        }

        return ret;
    }