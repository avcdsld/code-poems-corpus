public void importVocabulary(@NonNull VocabCache<T> vocabCache) {
        AtomicBoolean added = new AtomicBoolean(false);
        for (T element : vocabCache.vocabWords()) {
            if (this.addToken(element))
                added.set(true);
        }
        //logger.info("Current state: {}; Adding value: {}", this.documentsCounter.get(), vocabCache.totalNumberOfDocs());
        if (added.get())
            this.documentsCounter.addAndGet(vocabCache.totalNumberOfDocs());
    }