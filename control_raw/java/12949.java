public static Expression createExpressionForField(FieldExtension fieldExtension) {
        if (StringUtils.isNotEmpty(fieldExtension.getExpression())) {
            ExpressionManager expressionManager = Context.getProcessEngineConfiguration().getExpressionManager();
            return expressionManager.createExpression(fieldExtension.getExpression());
        } else {
            return new FixedValue(fieldExtension.getStringValue());
        }
    }