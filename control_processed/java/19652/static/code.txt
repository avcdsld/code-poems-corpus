private static boolean multiplyAndSubtractUnsignedMultiPrecision(int[] left, int leftOffset, int[] right, int length, int multiplier)
    {
        long unsignedMultiplier = multiplier & LONG_MASK;
        int leftIndex = leftOffset - length;
        long multiplyAccumulator = 0;
        long subtractAccumulator = INT_BASE;
        for (int rightIndex = 0; rightIndex < length; rightIndex++, leftIndex++) {
            multiplyAccumulator = (right[rightIndex] & LONG_MASK) * unsignedMultiplier + multiplyAccumulator;
            subtractAccumulator = (subtractAccumulator + (left[leftIndex] & LONG_MASK)) - (lowInt(multiplyAccumulator) & LONG_MASK);
            multiplyAccumulator = (multiplyAccumulator >>> 32);
            left[leftIndex] = lowInt(subtractAccumulator);
            subtractAccumulator = (subtractAccumulator >>> 32) + INT_BASE - 1;
        }
        subtractAccumulator += (left[leftIndex] & LONG_MASK) - multiplyAccumulator;
        left[leftIndex] = lowInt(subtractAccumulator);
        return highInt(subtractAccumulator) == 0;
    }