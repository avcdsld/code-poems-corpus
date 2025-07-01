public Future<Pair<String, INDArray>> inferVectorBatched(@NonNull LabelledDocument document) {
        if (countSubmitted == null)
            initInference();

        if (this.vocab == null || this.vocab.numWords() == 0)
            reassignExistingModel();

        // we block execution until queued amount of documents gets below acceptable level, to avoid memory exhaust
        while (countSubmitted.get() - countFinished.get() > 1024) {
            ThreadUtils.uncheckedSleep(50);
        }

        InferenceCallable callable = new InferenceCallable(vocab, tokenizerFactory, document);
        Future<Pair<String, INDArray>> future = inferenceExecutor.submit(callable);
        countSubmitted.incrementAndGet();

        return future;
    }