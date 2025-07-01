public static <K, VV, EV> Graph<K, VV, EV> fromCollection(Collection<Edge<K, EV>> edges,
			final MapFunction<K, VV> vertexValueInitializer, ExecutionEnvironment context) {

		return fromDataSet(context.fromCollection(edges), vertexValueInitializer, context);
	}