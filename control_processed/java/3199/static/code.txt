@Override
	public void collect(T record)  {
		if (record != null) {
			this.delegate.setInstance(record);
			try {
				for (RecordWriter<SerializationDelegate<T>> writer : writers) {
					writer.emit(this.delegate);
				}
			}
			catch (IOException e) {
				throw new RuntimeException("Emitting the record caused an I/O exception: " + e.getMessage(), e);
			}
			catch (InterruptedException e) {
				throw new RuntimeException("Emitting the record was interrupted: " + e.getMessage(), e);
			}
		}
		else {
			throw new NullPointerException("The system does not support records that are null."
								+ "Null values are only supported as fields inside other objects.");
		}
	}