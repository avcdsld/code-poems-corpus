public byte getByte(String key) {
		addToDefaults(key, null);
		String value = getRequired(key);
		return Byte.valueOf(value);
	}