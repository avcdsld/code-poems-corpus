public void toggleTabNames(boolean showTabNames) {
		if (this.showTabNames == showTabNames) {
			return;
		}

		this.showTabNames = showTabNames;

		responseTabbedPanel.setShowTabNames(showTabNames);

		if (layout != Layout.FULL) {
			getTabbedStatus().setShowTabNames(showTabNames);
			getTabbedSelect().setShowTabNames(showTabNames);
			getTabbedWork().setShowTabNames(showTabNames);
		} else {
			getTabbedFull().setShowTabNames(showTabNames);
		}
	}