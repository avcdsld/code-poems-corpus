private Graph<K, VV, EV> removeVertices(DataSet<Vertex<K, VV>> verticesToBeRemoved) {

		DataSet<Vertex<K, VV>> newVertices = getVertices().coGroup(verticesToBeRemoved).where(0).equalTo(0)
				.with(new VerticesRemovalCoGroup<>()).name("Remove vertices");

		DataSet <Edge< K, EV>> newEdges = newVertices.join(getEdges()).where(0).equalTo(0)
				// if the edge source was removed, the edge will also be removed
				.with(new ProjectEdgeToBeRemoved<>()).name("Edges to be removed")
				// if the edge target was removed, the edge will also be removed
				.join(newVertices).where(1).equalTo(0)
				.with(new ProjectEdge<>()).name("Remove edges");

		return new Graph<>(newVertices, newEdges, context);
	}