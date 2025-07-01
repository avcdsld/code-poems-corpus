public Collection<String> getStringCollection(String name) {
		String valueString = get(name);
		return StringUtils.getStringCollection(valueString);
	}