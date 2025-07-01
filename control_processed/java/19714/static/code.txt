public Expression rewriteExpressionAllowNonDeterministic(Expression expression, Predicate<Symbol> symbolScope)
    {
        return rewriteExpression(expression, symbolScope, true);
    }