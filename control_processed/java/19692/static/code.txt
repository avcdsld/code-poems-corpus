private SymbolStatsEstimate normalizeSymbolStats(Symbol symbol, SymbolStatsEstimate symbolStats, PlanNodeStatsEstimate stats, TypeProvider types)
    {
        if (symbolStats.isUnknown()) {
            return SymbolStatsEstimate.unknown();
        }

        double outputRowCount = stats.getOutputRowCount();
        checkArgument(outputRowCount > 0, "outputRowCount must be greater than zero: %s", outputRowCount);
        double distinctValuesCount = symbolStats.getDistinctValuesCount();
        double nullsFraction = symbolStats.getNullsFraction();

        if (!isNaN(distinctValuesCount)) {
            Type type = requireNonNull(types.get(symbol), () -> "type is missing for symbol " + symbol);
            double maxDistinctValuesByLowHigh = maxDistinctValuesByLowHigh(symbolStats, type);
            if (distinctValuesCount > maxDistinctValuesByLowHigh) {
                distinctValuesCount = maxDistinctValuesByLowHigh;
            }

            if (distinctValuesCount > outputRowCount) {
                distinctValuesCount = outputRowCount;
            }

            double nonNullValues = outputRowCount * (1 - nullsFraction);
            if (distinctValuesCount > nonNullValues) {
                double difference = distinctValuesCount - nonNullValues;
                distinctValuesCount -= difference / 2;
                nonNullValues += difference / 2;
                nullsFraction = 1 - nonNullValues / outputRowCount;
            }
        }

        if (distinctValuesCount == 0.0) {
            return SymbolStatsEstimate.zero();
        }

        return SymbolStatsEstimate.buildFrom(symbolStats)
                .setDistinctValuesCount(distinctValuesCount)
                .setNullsFraction(nullsFraction)
                .build();
    }