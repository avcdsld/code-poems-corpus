public List<SiteNode> getNodesInContextFromSiteTree() {
		List<SiteNode> nodes = new LinkedList<>();
		SiteNode rootNode = session.getSiteTree().getRoot();
		fillNodesInContext(rootNode, nodes);
		return nodes;
	}