public void addDefaultKryoSerializer(Class<?> type, Class<? extends Serializer<?>> serializerClass) {
		if (type == null || serializerClass == null) {
			throw new NullPointerException("Cannot register null class or serializer.");
		}
		defaultKryoSerializerClasses.put(type, serializerClass);
	}