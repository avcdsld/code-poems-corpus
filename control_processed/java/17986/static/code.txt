public static void assertSameLength(INDArray x, INDArray z) {
        val lengthX = x.length();
        val lengthZ = z.length();
        if (lengthX != lengthZ && lengthX != 1 && lengthZ != 1)
            throw new IllegalStateException("Mis matched lengths: [" + x.length() + "] != [" + z.length() + "] - " +
                    "Array 1 shape: " + Arrays.toString(x.shape()) + ", array 2 shape: " + Arrays.toString(z.shape()));
    }