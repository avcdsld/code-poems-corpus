@SafeVarargs
	public final <X> DataSource<X> fromElements(X... data) {
		if (data == null) {
			throw new IllegalArgumentException("The data must not be null.");
		}
		if (data.length == 0) {
			throw new IllegalArgumentException("The number of elements must not be zero.");
		}

		TypeInformation<X> typeInfo;
		try {
			typeInfo = TypeExtractor.getForObject(data[0]);
		}
		catch (Exception e) {
			throw new RuntimeException("Could not create TypeInformation for type " + data[0].getClass().getName()
					+ "; please specify the TypeInformation manually via "
					+ "ExecutionEnvironment#fromElements(Collection, TypeInformation)", e);
		}

		return fromCollection(Arrays.asList(data), typeInfo, Utils.getCallLocationName());
	}