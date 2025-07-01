public CircuitBreakerRegistry createCircuitBreakerRegistry(CircuitBreakerConfigurationProperties circuitBreakerProperties) {
		Map<String, CircuitBreakerConfig> configs = circuitBreakerProperties.getConfigs()
				.entrySet().stream().collect(Collectors.toMap(Map.Entry::getKey,
						entry -> circuitBreakerProperties.createCircuitBreakerConfig(entry.getValue())));

		return CircuitBreakerRegistry.of(configs);
	}