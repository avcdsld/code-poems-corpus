public int indexOf(final byte b, final int from, final int to) {
        int beginIndex = from;
        if (beginIndex < 0) {
            beginIndex = 0;
        }
        int endIndex = to;
        if (endIndex > this.len) {
            endIndex = this.len;
        }
        if (beginIndex > endIndex) {
            return -1;
        }
        for (int i = beginIndex; i < endIndex; i++) {
            if (this.array[i] == b) {
                return i;
            }
        }
        return -1;
    }