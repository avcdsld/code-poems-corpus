public static List<List<Writable>> convertStringInput(List<List<String>> stringInput,Schema schema) {
        List<List<Writable>> ret = new ArrayList<>();
        List<List<Writable>> timeStepAdd = new ArrayList<>();
        for(int j = 0; j < stringInput.size(); j++) {
            List<String> record = stringInput.get(j);
            List<Writable> recordAdd = new ArrayList<>();
            for(int k = 0; k < record.size(); k++) {
                switch(schema.getType(k)) {
                    case Double: recordAdd.add(new DoubleWritable(Double.parseDouble(record.get(k)))); break;
                    case Float:  recordAdd.add(new FloatWritable(Float.parseFloat(record.get(k)))); break;
                    case Integer:  recordAdd.add(new IntWritable(Integer.parseInt(record.get(k)))); break;
                    case Long:  recordAdd.add(new LongWritable(Long.parseLong(record.get(k)))); break;
                    case String: recordAdd.add(new Text(record.get(k))); break;
                    case Time: recordAdd.add(new LongWritable(Long.parseLong(record.get(k)))); break;

                }
            }

            timeStepAdd.add(recordAdd);
        }


        return ret;
    }