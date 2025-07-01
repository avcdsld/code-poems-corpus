public static <T> T[] shuffle(T[] array, Random random) {
		if (array != null && array.length > 1 && random != null) {
			for (int i = array.length; i > 1; i--) {
				swap(array, i - 1, random.nextInt(i));
			}
		}
		return array;
	}