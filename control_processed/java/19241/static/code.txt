@Override
    public void close() {
        if (trainingArchive != null && trainingArchive != weightsArchive) {
            trainingArchive.close();
            trainingArchive = null;
        }
        if (weightsArchive != null) {
            weightsArchive.close();
            weightsArchive = null;
        }
    }