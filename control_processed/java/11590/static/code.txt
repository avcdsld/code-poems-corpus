static synchronized void clearTLDOverrides() {
        inUse = false;
        countryCodeTLDsPlus = MemoryReductionUtil.EMPTY_STRING_ARRAY;
        countryCodeTLDsMinus = MemoryReductionUtil.EMPTY_STRING_ARRAY;
        genericTLDsPlus = MemoryReductionUtil.EMPTY_STRING_ARRAY;
        genericTLDsMinus = MemoryReductionUtil.EMPTY_STRING_ARRAY;
    }