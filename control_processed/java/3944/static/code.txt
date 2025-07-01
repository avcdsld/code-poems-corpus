private O setResources(ResourceSpec resources) {
		Preconditions.checkNotNull(resources, "The resources must be not null.");
		Preconditions.checkArgument(resources.isValid(), "The values in resources must be not less than 0.");

		this.minResources = resources;
		this.preferredResources = resources;

		@SuppressWarnings("unchecked")
		O returnType = (O) this;
		return returnType;
	}