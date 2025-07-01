@Override
    public double similarity(Vertex<V> vertex1, Vertex<V> vertex2) {
        return similarity(vertex1.vertexID(), vertex2.vertexID());
    }