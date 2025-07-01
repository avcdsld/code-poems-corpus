public void rebuildDependencyGraph() {
        DependencyGraph graph = new DependencyGraph();
        graph.build();
        // volatile acts a as a memory barrier here and therefore guarantees
        // that graph is fully build, before it's visible to other threads
        dependencyGraph = graph;
        dependencyGraphDirty.set(false);
    }