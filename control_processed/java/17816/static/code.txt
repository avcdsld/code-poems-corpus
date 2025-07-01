public SDVariable oneHot(String name, SDVariable indices, int depth, int axis, double on, double off) {
        return oneHot(name, indices, depth, axis, on, off, OneHot.DEFAULT_DTYPE);
    }