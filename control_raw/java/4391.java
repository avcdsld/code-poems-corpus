public static NestedSerializersSnapshotDelegate readNestedSerializerSnapshots(DataInputView in, ClassLoader cl) throws IOException {
		final int magicNumber = in.readInt();
		if (magicNumber != MAGIC_NUMBER) {
			throw new IOException(String.format("Corrupt data, magic number mismatch. Expected %8x, found %8x",
					MAGIC_NUMBER, magicNumber));
		}

		final int version = in.readInt();
		if (version != VERSION) {
			throw new IOException("Unrecognized version: " + version);
		}

		final int numSnapshots = in.readInt();
		final TypeSerializerSnapshot<?>[] nestedSnapshots = new TypeSerializerSnapshot<?>[numSnapshots];

		for (int i = 0; i < numSnapshots; i++) {
			nestedSnapshots[i] = TypeSerializerSnapshot.readVersionedSnapshot(in, cl);
		}

		return new NestedSerializersSnapshotDelegate(nestedSnapshots);
	}