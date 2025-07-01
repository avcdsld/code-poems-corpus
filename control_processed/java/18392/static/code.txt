public long getTotalMemoryBytes(int minibatchSize, @NonNull MemoryUseMode memoryUseMode,
                    @NonNull CacheMode cacheMode) {
        return getTotalMemoryBytes(minibatchSize, memoryUseMode, cacheMode, DataTypeUtil.getDtypeFromContext());
    }