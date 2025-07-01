public static void set(final int[][] array, final long index, int value)
    {
        array[segment(index)][displacement(index)] = value;
    }