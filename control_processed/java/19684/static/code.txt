private void initialize()
    {
        activeOperators.stream()
                .map(Operator::getOperatorContext)
                .forEach(operatorContext -> operatorContext.setMemoryRevocationRequestListener(() -> driverBlockedFuture.get().set(null)));
    }