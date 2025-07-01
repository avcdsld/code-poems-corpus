@Override
    public Object map(Object input) {
        Number n = (Number) input;
        if (inputSchema.getMetaData(columnNumber).isValid(new IntWritable(n.intValue()))) {
            return input;
        } else {
            return value;
        }
    }