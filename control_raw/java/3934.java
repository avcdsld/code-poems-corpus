public static <K, VV, Message, EV> ScatterGatherIteration<K, VV, Message, EV> withEdges(
			DataSet<Edge<K, EV>> edgesWithValue, ScatterFunction<K, VV, Message, EV> sf,
			GatherFunction<K, VV, Message> gf, int maximumNumberOfIterations) {

		return new ScatterGatherIteration<>(sf, gf, edgesWithValue, maximumNumberOfIterations);
	}