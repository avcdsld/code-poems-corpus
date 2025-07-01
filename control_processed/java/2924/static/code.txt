void removeEntry(NodeId nodeId) throws Exception {
		this.entryCache.remove(nodeId);
		this.entries.remove(nodeId);
	}