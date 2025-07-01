public boolean hasAbsentKeysOrValues() {
		for (Entry<String, KeyValue<K, V>> entry : underlyingMap.entrySet()) {
			if (keyOrValueIsAbsent(entry)) {
				return true;
			}
		}
		return false;
	}