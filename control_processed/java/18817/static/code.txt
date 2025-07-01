public static void validateCnn1DKernelStridePadding(int kernel, int stride, int padding) {

        if (kernel <= 0) {
            throw new IllegalStateException("Invalid kernel size: value must be positive (> 0). Got: " + kernel);
        }
        if (stride <= 0) {
            throw new IllegalStateException("Invalid kernel size: value must be positive (> 0). Got: " + stride);

        }
        if (padding < 0) {
            throw new IllegalStateException("Invalid kernel size: value must be positive (> 0). Got: " + padding);
        }
    }