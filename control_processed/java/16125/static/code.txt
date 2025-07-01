public static <T> Flux<T> toFlux(EventPublisher<T> eventPublisher) {
        DirectProcessor<T> directProcessor = DirectProcessor.create();
        eventPublisher.onEvent(directProcessor::onNext);
        return directProcessor;
    }