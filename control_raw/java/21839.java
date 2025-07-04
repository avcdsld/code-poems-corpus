public static <T> T[] concat(T[] a, T... b) {
        int aLen = a.length;
        int bLen = b.length;

        if (bLen == 0) {
            return a;
        }
        if (aLen == 0) {
            return b;
        }

        @SuppressWarnings("unchecked")
        T[] c = (T[]) Array.newInstance(a.getClass().getComponentType(), aLen + bLen);
        System.arraycopy(a, 0, c, 0, aLen);
        System.arraycopy(b, 0, c, aLen, bLen);

        return c;
    }