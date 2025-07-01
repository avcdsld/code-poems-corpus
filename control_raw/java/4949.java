public static MemorySize parse(String text, MemoryUnit defaultUnit) throws IllegalArgumentException {
		if (!hasUnit(text)) {
			return parse(text + defaultUnit.getUnits()[0]);
		}

		return parse(text);
	}