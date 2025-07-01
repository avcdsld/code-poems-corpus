private void writeObject(ObjectOutputStream out) throws IOException {
		out.defaultWriteObject();

		final int size = dataSet.size();
		out.writeInt(size);

		if (size > 0) {
			DataOutputViewStreamWrapper wrapper = new DataOutputViewStreamWrapper(out);
			for (T element : dataSet){
				serializer.serialize(element, wrapper);
			}
		}
	}