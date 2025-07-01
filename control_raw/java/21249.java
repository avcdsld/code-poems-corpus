protected void updateFoundCount() {
		SpiderScan sc = this.getSelectedScanner();
		if (sc != null) {
			this.getFoundCountValueLabel().setText(Integer.toString(sc.getNumberOfURIsFound()));
		} else {
			this.getFoundCountValueLabel().setText(ZERO_REQUESTS_LABEL_TEXT);
		}
	}