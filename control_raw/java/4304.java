private boolean containsKey(K key, int keyGroupIndex, N namespace) {

		checkKeyNamespacePreconditions(key, namespace);

		Map<N, Map<K, S>> namespaceMap = getMapForKeyGroup(keyGroupIndex);

		if (namespaceMap == null) {
			return false;
		}

		Map<K, S> keyedMap = namespaceMap.get(namespace);

		return keyedMap != null && keyedMap.containsKey(key);
	}