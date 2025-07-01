private static GroupTemplate createGroupTemplate(ResourceLoader loader) {
		try {
			return createGroupTemplate(loader, Configuration.defaultConfiguration());
		} catch (IOException e) {
			throw new IORuntimeException(e);
		}
	}