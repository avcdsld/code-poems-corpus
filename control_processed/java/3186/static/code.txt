public static void tryDeserializeAndThrow(Throwable throwable, ClassLoader classLoader) throws Throwable {
		Throwable current = throwable;

		while (!(current instanceof SerializedThrowable) && current.getCause() != null) {
			current = current.getCause();
		}

		if (current instanceof SerializedThrowable) {
			throw ((SerializedThrowable) current).deserializeError(classLoader);
		} else {
			throw throwable;
		}
	}