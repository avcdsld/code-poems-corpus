private static int maxLength(List<String> coll) {
		int max = 0;
		for (String e : coll) {
			int length = e.length();
			if (length > max) {
				max = length;
			}
		}
		return max;
	}