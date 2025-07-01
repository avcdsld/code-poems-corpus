public static CircuitBreakerExports ofCircuitBreakerRegistry(String prefix, CircuitBreakerRegistry circuitBreakerRegistry) {
        requireNonNull(prefix);
        requireNonNull(circuitBreakerRegistry);
        return new CircuitBreakerExports(prefix, circuitBreakerRegistry);
    }