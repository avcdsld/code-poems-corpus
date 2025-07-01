@Override
	public Object handle(ProceedingJoinPoint proceedingJoinPoint, CircuitBreaker circuitBreaker, String methodName) throws Throwable {
		Object returnValue = proceedingJoinPoint.proceed();
		if (Flux.class.isAssignableFrom(returnValue.getClass())) {
			Flux<?> fluxReturnValue = (Flux<?>) returnValue;
			return fluxReturnValue.transform(io.github.resilience4j.reactor.circuitbreaker.operator.CircuitBreakerOperator.of(circuitBreaker));
		} else if (Mono.class.isAssignableFrom(returnValue.getClass())) {
			Mono<?> monoReturnValue = (Mono<?>) returnValue;
			return monoReturnValue.transform(CircuitBreakerOperator.of(circuitBreaker));
		} else {
			logger.error("Unsupported type for Reactor circuit breaker {}", returnValue.getClass().getTypeName());
			throw new IllegalArgumentException("Not Supported type for the circuit breaker in Reactor:" + returnValue.getClass().getName());

		}
	}