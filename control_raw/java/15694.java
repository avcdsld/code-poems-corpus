public static Set<String> getRequiredFields(Query query)
  {
    Set<String> dimensions = new HashSet<>();
    Set<String> dimsInFilter = null == query.getFilter() ? new HashSet<String>() : query.getFilter().getRequiredColumns();
    dimensions.addAll(dimsInFilter);

    if (query instanceof TopNQuery) {
      TopNQuery q = (TopNQuery) query;
      dimensions.addAll(extractFieldsFromAggregations(q.getAggregatorSpecs()));
      dimensions.add(q.getDimensionSpec().getDimension());
    } else if (query instanceof TimeseriesQuery) {
      TimeseriesQuery q = (TimeseriesQuery) query;
      dimensions.addAll(extractFieldsFromAggregations(q.getAggregatorSpecs()));
    } else if (query instanceof GroupByQuery) {
      GroupByQuery q = (GroupByQuery) query;
      dimensions.addAll(extractFieldsFromAggregations(q.getAggregatorSpecs()));
      for (DimensionSpec spec : q.getDimensions()) {
        String dim = spec.getDimension();
        dimensions.add(dim);
      }
    } else {
      throw new UnsupportedOperationException("Method getRequeiredFields only support TopNQuery/TimeseriesQuery/GroupByQuery");
    }
    return dimensions;
  }