public static int nextInt(Random random, int min, int max) {
		Validate.isTrue(max >= min, "Start value must be smaller or equal to end value.");
		MoreValidate.nonNegative("min", min);

		if (min == max) {
			return min;
		}

		return min + random.nextInt(max - min);
	}