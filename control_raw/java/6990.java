public T header(Header name, String value, boolean isOverride) {
		return header(name.toString(), value, isOverride);
	}