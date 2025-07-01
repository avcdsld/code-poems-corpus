public static Writable fromEntry(int item,FieldVector from,ColumnType columnType) {
        if(from.getValueCount() < item) {
            throw new IllegalArgumentException("Index specified greater than the number of items in the vector with length " + from.getValueCount());
        }

        switch(columnType) {
            case Integer:
                return new IntWritable(getIntFromFieldVector(item,from));
            case Long:
                return new LongWritable(getLongFromFieldVector(item,from));
            case Float:
                return new FloatWritable(getFloatFromFieldVector(item,from));
            case Double:
                return new DoubleWritable(getDoubleFromFieldVector(item,from));
            case Boolean:
                BitVector bitVector = (BitVector) from;
                return new BooleanWritable(bitVector.get(item) > 0);
            case Categorical:
                VarCharVector varCharVector = (VarCharVector) from;
                return new Text(varCharVector.get(item));
            case String:
                VarCharVector varCharVector2 = (VarCharVector) from;
                return new Text(varCharVector2.get(item));
            case Time:
                //TODO: need to look at closer
                return new LongWritable(getLongFromFieldVector(item,from));
            case NDArray:
                VarBinaryVector valueVector = (VarBinaryVector) from;
                byte[] bytes = valueVector.get(item);
                ByteBuffer direct = ByteBuffer.allocateDirect(bytes.length);
                direct.put(bytes);
                INDArray fromTensor = BinarySerde.toArray(direct);
                return new NDArrayWritable(fromTensor);
            default:
                throw new IllegalArgumentException("Illegal type " + from.getClass().getName());
        }
    }