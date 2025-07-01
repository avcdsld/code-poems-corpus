public SDVariable oneHot(String name, SDVariable indices, int depth) {
        return oneHot(name, indices, depth, -1, 1.00, 0.00);
    }