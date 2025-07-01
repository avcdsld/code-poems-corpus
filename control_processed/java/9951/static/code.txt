public static Optional<Condition> createBetweenCondition(final PredicateBetweenRightValue betweenRightValue, final Column column) {
        return betweenRightValue.getBetweenExpression() instanceof SimpleExpressionSegment && betweenRightValue.getAndExpression() instanceof SimpleExpressionSegment
                ? Optional.of(new Condition(column,
                ((SimpleExpressionSegment) betweenRightValue.getBetweenExpression()).getSQLExpression(), ((SimpleExpressionSegment) betweenRightValue.getAndExpression()).getSQLExpression()))
                : Optional.<Condition>absent();
    }