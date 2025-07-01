private static int[] createIncrIntArray(int numKeys) {
		int[] keyFields = new int[numKeys];
		for (int i = 0; i < numKeys; i++) {
			keyFields[i] = i;
		}
		return keyFields;
	}