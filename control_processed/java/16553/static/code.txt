public static int[] stride(INDArray arr, INDArrayIndex[] indexes, int... shape) {
        List<Integer> strides = new ArrayList<>();
        int strideIndex = 0;
        //list of indexes to prepend to for new axes
        //if all is encountered
        List<Integer> prependNewAxes = new ArrayList<>();

        for (int i = 0; i < indexes.length; i++) {
            //just like the shape, drops the stride
            if (indexes[i] instanceof PointIndex) {
                strideIndex++;
                continue;
            } else if (indexes[i] instanceof NewAxis) {

            }
        }

        /**
         * For each dimension
         * where we want to prepend a dimension
         * we need to add it at the index such that
         * we account for the offset of the number of indexes
         * added up to that point.
         *
         * We do this by doing an offset
         * for each item added "so far"
         *
         * Note that we also have an offset of - 1
         * because we want to prepend to the given index.
         *
         * When prepend new axes for in the middle is triggered
         * i is already > 0
         */
        for (int i = 0; i < prependNewAxes.size(); i++) {
            strides.add(prependNewAxes.get(i) - i, 1);
        }

        return Ints.toArray(strides);

    }