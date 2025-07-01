private void validateTabbed(int tabIndex) {
		if (!isTabbed()) {
			throw new IllegalArgumentException("Not initialised as a tabbed dialog - must use method without tab parameters");
		}
		if (tabIndex < 0 || tabIndex >= this.tabPanels.size()) {
			throw new IllegalArgumentException("Invalid tab index: " + tabIndex);
		}
	}