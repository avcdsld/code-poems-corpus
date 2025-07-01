public static Call.Mapper<List<List<Span>>, List<List<Span>>> create(QueryRequest request) {
    return new FilterTraces(request);
  }