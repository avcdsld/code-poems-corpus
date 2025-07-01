@Override
    public boolean condition(Object input) {
        if (input instanceof String) {
            return !schema.getMetaData(columnIdx).isValid(new Text(input.toString()));
        } else if (input instanceof Double) {
            Double d = (Double) input;
            return !schema.getMetaData(columnIdx).isValid(new DoubleWritable(d));
        } else if (input instanceof Integer) {
            Integer i = (Integer) input;
            return !schema.getMetaData(columnIdx).isValid(new IntWritable(i));
        } else if (input instanceof Long) {
            Long l = (Long) input;
            return !schema.getMetaData(columnIdx).isValid(new LongWritable(l));
        } else if (input instanceof Boolean) {
            Boolean b = (Boolean) input;
            return !schema.getMetaData(columnIdx).isValid(new BooleanWritable(b));
        }

        else
            throw new IllegalStateException("Illegal type " + input.getClass().toString());
    }