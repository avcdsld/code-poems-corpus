public static <K, VV, EV> Graph<K, VV, EV> fromCollection(Collection<Vertex<K, VV>> vertices,
			Collection<Edge<K, EV>> edges, ExecutionEnvironment context) {

		return fromDataSet(context.fromCollection(vertices),
				context.fromCollection(edges), context);
	}