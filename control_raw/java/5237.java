public V get(K key) {
		final int hash = hash(key);
		final int slot = indexOf(hash);

		// search the chain from the slot
		for (Entry<K, V> entry = table[slot]; entry != null; entry = entry.next) {
			if (entry.hashCode == hash && entry.key.equals(key)) {
				return entry.value;
			}
		}

		// not found
		return null;
	}