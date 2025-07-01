public static void convert(RecordReader reader, RecordWriter writer, boolean closeOnCompletion) throws IOException {

        if(!reader.hasNext()){
            throw new UnsupportedOperationException("Cannot convert RecordReader: reader has no next element");
        }

        while(reader.hasNext()){
            writer.write(reader.next());
        }

        if(closeOnCompletion){
            writer.close();
        }
    }