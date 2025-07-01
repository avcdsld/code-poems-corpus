public static int readInt(ArrayView source, int position) {
        return (source.get(position) & 0xFF) << 24
                | (source.get(position + 1) & 0xFF) << 16
                | (source.get(position + 2) & 0xFF) << 8
                | (source.get(position + 3) & 0xFF);
    }