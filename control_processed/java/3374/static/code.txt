public TypeInformation<?>[] getParameterTypes(Class<?>[] signature) {
		final TypeInformation<?>[] types = new TypeInformation<?>[signature.length];
		for (int i = 0; i < signature.length; i++) {
			try {
				types[i] = TypeExtractor.getForClass(signature[i]);
			} catch (InvalidTypesException e) {
				throw new ValidationException(
					"Parameter types of scalar function " + this.getClass().getCanonicalName() +
					" cannot be automatically determined. Please provide type information manually.");
			}
		}
		return types;
	}