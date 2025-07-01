private PlanBuilder appendExistSubqueryApplyNode(PlanBuilder subPlan, ExistsPredicate existsPredicate, boolean correlationAllowed)
    {
        if (subPlan.canTranslate(existsPredicate)) {
            // given subquery is already appended
            return subPlan;
        }

        PlanBuilder subqueryPlan = createPlanBuilder(existsPredicate.getSubquery());

        PlanNode subqueryPlanRoot = subqueryPlan.getRoot();
        if (isAggregationWithEmptyGroupBy(subqueryPlanRoot)) {
            subPlan.getTranslations().put(existsPredicate, BooleanLiteral.TRUE_LITERAL);
            return subPlan;
        }

        // add an explicit projection that removes all columns
        PlanNode subqueryNode = new ProjectNode(idAllocator.getNextId(), subqueryPlan.getRoot(), Assignments.of());

        Symbol exists = symbolAllocator.newSymbol("exists", BOOLEAN);
        subPlan.getTranslations().put(existsPredicate, exists);
        ExistsPredicate rewrittenExistsPredicate = new ExistsPredicate(BooleanLiteral.TRUE_LITERAL);
        return appendApplyNode(
                subPlan,
                existsPredicate.getSubquery(),
                subqueryNode,
                Assignments.of(exists, rewrittenExistsPredicate),
                correlationAllowed);
    }