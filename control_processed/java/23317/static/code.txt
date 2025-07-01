public static long nextLong(Random random, long min, long max) {
		Validate.isTrue(max >= min, "Start value must be smaller or equal to end value.");
		MoreValidate.nonNegative("min", min);

		if (min == max) {
			return min;
		}

		return (long) (min + ((max - min) * random.nextDouble()));
	}