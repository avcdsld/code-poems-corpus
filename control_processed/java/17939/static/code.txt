public SingleCSVRecord transform(SingleCSVRecord record) {
        List<Writable> record2 = toArrowWritablesSingle(
                toArrowColumnsStringSingle(bufferAllocator,
                        transformProcess.getInitialSchema(),record.getValues()),
                transformProcess.getInitialSchema());
        List<Writable> finalRecord = execute(Arrays.asList(record2),transformProcess).get(0);
        String[] values = new String[finalRecord.size()];
        for (int i = 0; i < values.length; i++)
            values[i] = finalRecord.get(i).toString();
        return new SingleCSVRecord(values);

    }