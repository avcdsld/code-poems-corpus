public Expression rewriteExpression(Expression expression, Predicate<Symbol> symbolScope)
    {
        checkArgument(isDeterministic(expression), "Only deterministic expressions may be considered for rewrite");
        return rewriteExpression(expression, symbolScope, true);
    }