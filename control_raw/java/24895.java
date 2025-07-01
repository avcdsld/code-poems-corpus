public int bitLength() {
        if (bigVal != null) {
            return bigVal.bitLength();
        }
        if (val == 0 || val == -1) {
            return 0;
        }
        // Binary search for bit length
        int i = 32; // mask length
        long m = (1L << i) - 1; // AND mask with ones in little end
        if (val < 0) {
            m = ~m; // OR mask with ones in big end
            for (int j = i >> 1; j > 0; j >>= 1) { // mask delta
                if ((val | m) == val) { // mask >= enough
                    i -= j;
                    m >>= j; // try less bits
                } else {
                    i += j;
                    m <<= j; // try more bits
                }
            }
            if ((val | m) != val) {
                i++; // mask < enough
            }
        } else {
            for (int j = i >> 1; j > 0; j >>= 1) { // mask delta
                if ((val & m) == val) { // mask >= enough
                    i -= j;
                    m >>= j; // try less bits
                } else {
                    i += j;
                    m = m << j | m; // try more bits
                }
            }
            if ((val & m) != val) {
                i++; // mask < enough
            }
        }
        return i;
    }