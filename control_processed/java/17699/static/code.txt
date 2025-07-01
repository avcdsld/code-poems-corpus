public static INDArray toMmulCompatible(INDArray input) {
        if (input.rank() != 2)
            throw new IllegalArgumentException("Input must be rank 2 (matrix)");
        //Same conditions as GemmParams.copyIfNecessary()
        boolean doCopy = false;
        if (input.ordering() == 'c' && (input.stride(0) != input.size(1) || input.stride(1) != 1))
            doCopy = true;
        else if (input.ordering() == 'f' && (input.stride(0) != 1 || input.stride(1) != input.size(0)))
            doCopy = true;

        if (doCopy)
            return Shape.toOffsetZeroCopyAnyOrder(input);
        else
            return input;
    }