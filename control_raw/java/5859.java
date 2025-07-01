public void enableTimeToLive(StateTtlConfig ttlConfig) {
		Preconditions.checkNotNull(ttlConfig);
		Preconditions.checkArgument(
			ttlConfig.getUpdateType() != StateTtlConfig.UpdateType.Disabled &&
				queryableStateName == null,
			"Queryable state is currently not supported with TTL");
		this.ttlConfig = ttlConfig;
	}