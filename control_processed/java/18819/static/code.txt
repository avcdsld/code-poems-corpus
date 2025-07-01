@Override
    public void processEvent(ListenerEvent event, SequenceVectors<T> sequenceVectors, long argument) {
        try {
            locker.acquire();

            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");

            StringBuilder builder = new StringBuilder(targetFolder.getAbsolutePath());
            builder.append("/").append(modelPrefix).append("_").append(sdf.format(new Date())).append(".seqvec");
            File targetFile = new File(builder.toString());

            if (useBinarySerialization) {
                SerializationUtils.saveObject(sequenceVectors, targetFile);
            } else {
                throw new UnsupportedOperationException("Not implemented yet");
            }

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            locker.release();
        }
    }