public static long[] reductionShape(INDArray x, int[] dimension, boolean newFormat, boolean keepDims){
        boolean wholeArray = Shape.wholeArrayDimension(dimension) || dimension.length == x.rank();
        long[] retShape;
        if(!newFormat) {
            retShape = wholeArray ? new long[] {1, 1} : ArrayUtil.removeIndex(x.shape(), dimension);

            //ensure vector is proper shape (if old format)
            if (retShape.length == 1) {
                if (dimension[0] == 0)
                    retShape = new long[]{1, retShape[0]};
                else
                    retShape = new long[]{retShape[0], 1};
            } else if (retShape.length == 0) {
                retShape = new long[]{1, 1};
            }
        } else {
            if(keepDims){
                retShape = x.shape().clone();
                if(wholeArray){
                    for( int i=0; i<retShape.length; i++ ){
                        retShape[i] = 1;
                    }
                } else {
                    for (int d : dimension) {
                        retShape[d] = 1;
                    }
                }
            } else {
                retShape = wholeArray ? new long[0] : ArrayUtil.removeIndex(x.shape(), dimension);
            }
        }
        return retShape;
    }