public TableOperation createAggregate(
			List<Expression> groupings,
			List<Expression> aggregates,
			TableOperation child) {
		validateGroupings(groupings);
		validateAggregates(aggregates);

		List<PlannerExpression> convertedGroupings = bridge(groupings);
		List<PlannerExpression> convertedAggregates = bridge(aggregates);

		TypeInformation[] fieldTypes = Stream.concat(
			convertedGroupings.stream(),
			convertedAggregates.stream()
		).map(PlannerExpression::resultType)
			.toArray(TypeInformation[]::new);

		String[] fieldNames = Stream.concat(
			groupings.stream(),
			aggregates.stream()
		).map(expr -> extractName(expr).orElseGet(expr::toString))
			.toArray(String[]::new);

		TableSchema tableSchema = new TableSchema(fieldNames, fieldTypes);

		return new AggregateTableOperation(groupings, aggregates, child, tableSchema);
	}