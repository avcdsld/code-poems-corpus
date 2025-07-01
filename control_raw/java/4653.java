public static void checkArgument(boolean condition, @Nullable Object errorMessage) {
		if (!condition) {
			throw new IllegalArgumentException(String.valueOf(errorMessage));
		}
	}