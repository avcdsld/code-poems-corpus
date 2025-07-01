public void copy() throws Exception {
        if(callInitRecordReader) {
            if(recordReader != null) {
                recordReader.initialize(configuration, inputUrl);
            }
            else {
                if(readersToConcat == null || splitPerReader == null)  {
                    throw new IllegalArgumentException("No readers or input  splits found.");
                }

                if(readersToConcat.length != splitPerReader.length) {
                    throw new IllegalArgumentException("One input split must be specified per record reader");
                }

                for(int i = 0; i < readersToConcat.length; i++) {
                    if(readersToConcat[i] == null) {
                        throw new IllegalStateException("Reader at record " + i + " was null!");
                    }
                    if(splitPerReader[i] == null) {
                        throw new IllegalStateException("Split at " + i + " is null!");
                    }
                    //allow for, but do not enforce configurations per reader.
                    if(configurationsPerReader != null) {
                        readersToConcat[i].initialize(configurationsPerReader[i], splitPerReader[i]);
                    }
                    else {
                        readersToConcat[i].initialize(configuration,splitPerReader[i]);
                    }
                }
            }
        }

        if(callInitPartitioner) {
            partitioner.init(configuration, outputUrl);
        }

        if(callInitRecordWriter) {
            recordWriter.initialize(configuration, outputUrl, partitioner);
        }

        if(recordReader != null) {
            write(recordReader,true);
        }
        else if(readersToConcat != null) {
            for(RecordReader recordReader : readersToConcat) {
                write(recordReader,false);
            }

            //close since we can't do it within the method
            recordWriter.close();
        }

    }