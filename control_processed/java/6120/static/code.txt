public CsvReader includeFields(String mask) {
		boolean[] includedMask = new boolean[mask.length()];

		for (int i = 0; i < mask.length(); i++) {
			char c = mask.charAt(i);
			if (c == '1' || c == 'T' || c == 't') {
				includedMask[i] = true;
			} else if (c != '0' && c != 'F' && c != 'f') {
				throw new IllegalArgumentException("Mask string may contain only '0' and '1'.");
			}
		}

		return includeFields(includedMask);
	}