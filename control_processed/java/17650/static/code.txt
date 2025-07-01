public static long getOffset(IntBuffer shapeInformation, int row, int col) {
        int rank = rank(shapeInformation);
        if (rank != 2)
            throw new IllegalArgumentException(
                    "Cannot use this getOffset method on arrays of rank != 2 (rank is: " + rank + ")");
        long offset = 0;
        int size_0 = size(shapeInformation, 0);
        int size_1 = size(shapeInformation, 1);
        if (row >= size_0 || col >= size_1)
            throw new IllegalArgumentException("Invalid indices: cannot get [" + row + "," + col + "] from a "
                    + Arrays.toString(shape(shapeInformation)) + " NDArray");

        if (size_0 != 1)
            offset += row * stride(shapeInformation, 0);
        if (size_1 != 1)
            offset += col * stride(shapeInformation, 1);

        return offset;
    }