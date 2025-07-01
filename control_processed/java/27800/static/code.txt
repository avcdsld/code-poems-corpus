static String getPath(int nodeId, int depth) {
        StringBuilder pathBuilder = new StringBuilder();
        int value = nodeId;
        for (int i = 0; i < depth; i++) {
            int r = value % DIVISOR;
            value = value / DIVISOR;
            pathBuilder.append(SEPARATOR).append(r);
        }

        return pathBuilder.append(SEPARATOR).append(nodeId).toString();
    }