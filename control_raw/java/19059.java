@Override
    public DataBuffer createSame(DataBuffer buffer, boolean init) {
        switch (buffer.dataType()) {
            case INT:
                return createInt(buffer.length(), init);
            case FLOAT:
                return createFloat(buffer.length(), init);
            case DOUBLE:
                return createDouble(buffer.length(), init);
            case HALF:
                return createHalf(buffer.length(), init);
            default:
                throw new UnsupportedOperationException("Unknown dataType: " + buffer.dataType());
        }
    }