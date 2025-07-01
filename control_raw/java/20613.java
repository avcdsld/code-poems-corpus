protected void applyFilter (SiteNode node) {
    	if (filter != null) {
    		boolean filtered = this.setFilter(filter, node);
    		SiteNode parent = node.getParent();
    		if (parent != null && ! filtered && parent.isFiltered()) {
    			// This node is no longer filtered but its parent is, unfilter the parent so it becomes visible
    			this.clearParentFilter(parent);
    		}
    	} else {
    		node.setFiltered(false);
    	}
	}