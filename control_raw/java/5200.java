public RMatGraph<T> setNoise(boolean noiseEnabled, float noise) {
		Preconditions.checkArgument(noise >= 0.0f && noise <= 2.0f,
			"RMat parameter noise must be non-negative and less than or equal to 2.0");

		this.noiseEnabled = noiseEnabled;
		this.noise = noise;

		return this;
	}