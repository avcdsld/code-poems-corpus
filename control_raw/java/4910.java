public static void clipDBWithKeyGroupRange(
		@Nonnull RocksDB db,
		@Nonnull List<ColumnFamilyHandle> columnFamilyHandles,
		@Nonnull KeyGroupRange targetKeyGroupRange,
		@Nonnull KeyGroupRange currentKeyGroupRange,
		@Nonnegative int keyGroupPrefixBytes) throws RocksDBException {

		final byte[] beginKeyGroupBytes = new byte[keyGroupPrefixBytes];
		final byte[] endKeyGroupBytes = new byte[keyGroupPrefixBytes];

		if (currentKeyGroupRange.getStartKeyGroup() < targetKeyGroupRange.getStartKeyGroup()) {
			RocksDBKeySerializationUtils.serializeKeyGroup(
				currentKeyGroupRange.getStartKeyGroup(), beginKeyGroupBytes);
			RocksDBKeySerializationUtils.serializeKeyGroup(
				targetKeyGroupRange.getStartKeyGroup(), endKeyGroupBytes);
			deleteRange(db, columnFamilyHandles, beginKeyGroupBytes, endKeyGroupBytes);
		}

		if (currentKeyGroupRange.getEndKeyGroup() > targetKeyGroupRange.getEndKeyGroup()) {
			RocksDBKeySerializationUtils.serializeKeyGroup(
				targetKeyGroupRange.getEndKeyGroup() + 1, beginKeyGroupBytes);
			RocksDBKeySerializationUtils.serializeKeyGroup(
				currentKeyGroupRange.getEndKeyGroup() + 1, endKeyGroupBytes);
			deleteRange(db, columnFamilyHandles, beginKeyGroupBytes, endKeyGroupBytes);
		}
	}