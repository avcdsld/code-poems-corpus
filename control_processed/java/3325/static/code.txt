public static ResourceManagerId fromUuidOrNull(@Nullable UUID uuid) {
		return  uuid == null ? null : new ResourceManagerId(uuid);
	}