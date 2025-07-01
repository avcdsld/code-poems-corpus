@Override
	public Map<Integer, byte[]> traverseStreamGraphAndGenerateHashes(StreamGraph streamGraph) {
		// The hash function used to generate the hash
		final HashFunction hashFunction = Hashing.murmur3_128(0);
		final Map<Integer, byte[]> hashes = new HashMap<>();

		Set<Integer> visited = new HashSet<>();
		Queue<StreamNode> remaining = new ArrayDeque<>();

		// We need to make the source order deterministic. The source IDs are
		// not returned in the same order, which means that submitting the same
		// program twice might result in different traversal, which breaks the
		// deterministic hash assignment.
		List<Integer> sources = new ArrayList<>();
		for (Integer sourceNodeId : streamGraph.getSourceIDs()) {
			sources.add(sourceNodeId);
		}
		Collections.sort(sources);

		//
		// Traverse the graph in a breadth-first manner. Keep in mind that
		// the graph is not a tree and multiple paths to nodes can exist.
		//

		// Start with source nodes
		for (Integer sourceNodeId : sources) {
			remaining.add(streamGraph.getStreamNode(sourceNodeId));
			visited.add(sourceNodeId);
		}

		StreamNode currentNode;
		while ((currentNode = remaining.poll()) != null) {
			// Generate the hash code. Because multiple path exist to each
			// node, we might not have all required inputs available to
			// generate the hash code.
			if (generateNodeHash(currentNode, hashFunction, hashes, streamGraph.isChainingEnabled(), streamGraph)) {
				// Add the child nodes
				for (StreamEdge outEdge : currentNode.getOutEdges()) {
					StreamNode child = streamGraph.getTargetVertex(outEdge);

					if (!visited.contains(child.getId())) {
						remaining.add(child);
						visited.add(child.getId());
					}
				}
			} else {
				// We will revisit this later.
				visited.remove(currentNode.getId());
			}
		}

		return hashes;
	}