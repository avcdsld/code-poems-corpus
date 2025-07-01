private void parseBody() {
        if (currentStatus == MultiPartStatus.PREEPILOGUE || currentStatus == MultiPartStatus.EPILOGUE) {
            if (isLastChunk) {
                currentStatus = MultiPartStatus.EPILOGUE;
            }
            return;
        }
        parseBodyAttributes();
    }