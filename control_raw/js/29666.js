function(config) {
			if (config.env && typeof config.env === "object") {
				return this.merge(this.createEnvironmentConfig(config.env), config);
			}

			return config;
		}