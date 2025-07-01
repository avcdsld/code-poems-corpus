@Override
    public void incrementWordCount(String word, int increment) {
        T element = extendedVocabulary.get(word);
        if (element != null) {
            element.increaseElementFrequency(increment);
            totalWordCount.addAndGet(increment);
        }
    }