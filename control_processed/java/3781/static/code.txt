public static List<Tuple2<TypeSerializer<?>, TypeSerializerSnapshot<?>>> readSerializersAndConfigsWithResilience(
			DataInputView in,
			ClassLoader userCodeClassLoader) throws IOException {

		int numSerializersAndConfigSnapshots = in.readInt();

		int[] offsets = new int[numSerializersAndConfigSnapshots * 2];

		for (int i = 0; i < numSerializersAndConfigSnapshots; i++) {
			offsets[i * 2] = in.readInt();
			offsets[i * 2 + 1] = in.readInt();
		}

		int totalBytes = in.readInt();
		byte[] buffer = new byte[totalBytes];
		in.readFully(buffer);

		List<Tuple2<TypeSerializer<?>, TypeSerializerSnapshot<?>>> serializersAndConfigSnapshots =
			new ArrayList<>(numSerializersAndConfigSnapshots);

		TypeSerializer<?> serializer;
		TypeSerializerSnapshot<?> configSnapshot;
		try (
			ByteArrayInputStreamWithPos bufferWithPos = new ByteArrayInputStreamWithPos(buffer);
			DataInputViewStreamWrapper bufferWrapper = new DataInputViewStreamWrapper(bufferWithPos)) {

			for (int i = 0; i < numSerializersAndConfigSnapshots; i++) {

				bufferWithPos.setPosition(offsets[i * 2]);
				serializer = tryReadSerializer(bufferWrapper, userCodeClassLoader, true);

				bufferWithPos.setPosition(offsets[i * 2 + 1]);

				configSnapshot = TypeSerializerSnapshotSerializationUtil.readSerializerSnapshot(
						bufferWrapper, userCodeClassLoader, serializer);

				if (serializer instanceof LegacySerializerSnapshotTransformer) {
					configSnapshot = transformLegacySnapshot(serializer, configSnapshot);
				}

				serializersAndConfigSnapshots.add(new Tuple2<>(serializer, configSnapshot));
			}
		}

		return serializersAndConfigSnapshots;
	}