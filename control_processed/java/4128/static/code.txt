public <M> Graph<K, VV, EV> runScatterGatherIteration(
			ScatterFunction<K, VV, M, EV> scatterFunction,
			org.apache.flink.graph.spargel.GatherFunction<K, VV, M> gatherFunction,
			int maximumNumberOfIterations, ScatterGatherConfiguration parameters) {

		ScatterGatherIteration<K, VV, M, EV> iteration = ScatterGatherIteration.withEdges(
				edges, scatterFunction, gatherFunction, maximumNumberOfIterations);

		iteration.configure(parameters);

		DataSet<Vertex<K, VV>> newVertices = this.getVertices().runOperation(iteration);

		return new Graph<>(newVertices, this.edges, this.context);
	}