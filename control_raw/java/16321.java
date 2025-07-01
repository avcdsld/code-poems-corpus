public static INDArrayIndex interval(long begin, long stride, long end,long max) {
        if(begin < 0) {
            begin += max;
        }

        if(end < 0) {
            end += max;
        }

        if (Math.abs(begin - end) < 1)
            end++;
        if (stride > 1 && Math.abs(begin - end) == 1) {
            end *= stride;
        }
        return interval(begin, stride, end, false);
    }