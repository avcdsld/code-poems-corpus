@Bean
	@ConditionalOnMissingBean(value = RetryEvent.class, parameterizedContainer = EventConsumerRegistry.class)
	public EventConsumerRegistry<RetryEvent> retryEventConsumerRegistry() {
		return retryConfiguration.retryEventConsumerRegistry();
	}