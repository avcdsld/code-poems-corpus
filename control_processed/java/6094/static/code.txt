@SuppressWarnings({"unchecked", "deprecation"})
	private static <T> TypeSerializerSnapshot<T> configureForBackwardsCompatibility(
			TypeSerializerSnapshot<?> snapshot,
			TypeSerializer<?> serializer) {

		TypeSerializerSnapshot<T> typedSnapshot = (TypeSerializerSnapshot<T>) snapshot;
		TypeSerializer<T> typedSerializer = (TypeSerializer<T>) serializer;

		if (snapshot instanceof TypeSerializerConfigSnapshot) {
			((TypeSerializerConfigSnapshot<T>) typedSnapshot).setPriorSerializer(typedSerializer);
		}

		return typedSnapshot;
	}