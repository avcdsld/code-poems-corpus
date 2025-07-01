public static <K, V> HashMap<K, V> newHashMap(@NotNull final K[] keys, @NotNull final V[] values) {
		Validate.isTrue(keys.length == values.length, "keys.length is %d but values.length is %d", keys.length,
				values.length);

		HashMap<K, V> map = new HashMap<K, V>(keys.length * 2);

		for (int i = 0; i < keys.length; i++) {
			map.put(keys[i], values[i]);
		}

		return map;
	}