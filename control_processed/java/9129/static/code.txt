static void initPaths() {
		if (config != null && config.getPaths() != null) {
			for (PathChain pathChain : config.getPaths()) {
				pathChain.validate(configName + " config"); // raises exception on misconfiguration
				if(pathChain.getPath() == null) {
					addSourceChain(pathChain);
				} else {
					addPathChain(pathChain);
				}
			}
		}
	}