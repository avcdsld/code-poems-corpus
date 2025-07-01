public AdamicAdar<K, VV, EV> setMinimumScore(float score) {
		Preconditions.checkArgument(score >= 0, "Minimum score must be non-negative");

		this.minimumScore = score;

		return this;
	}