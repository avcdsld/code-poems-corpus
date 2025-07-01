private static <T> Map<Field, TypeSerializer<?>> buildNewFieldSerializersIndex(PojoSerializer<T> newPojoSerializer) {
		final Field[] newFields = newPojoSerializer.getFields();
		final TypeSerializer<?>[] newFieldSerializers = newPojoSerializer.getFieldSerializers();

		checkState(newFields.length == newFieldSerializers.length);

		int numFields = newFields.length;
		final Map<Field, TypeSerializer<?>> index = new HashMap<>(numFields);
		for (int i = 0; i < numFields; i++) {
			index.put(newFields[i], newFieldSerializers[i]);
		}

		return index;
	}