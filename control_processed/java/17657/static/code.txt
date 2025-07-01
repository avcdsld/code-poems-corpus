public static boolean isMatrix(IntBuffer shapeInfo) {
        int rank = Shape.rank(shapeInfo);
        if (rank != 2)
            return false;
        return !isVector(shapeInfo);
    }