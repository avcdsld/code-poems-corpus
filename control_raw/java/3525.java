@Override
	public D withSchema(Schema schema) {
		schemaDescriptor = Optional.of(Preconditions.checkNotNull(schema));
		return (D) this;
	}