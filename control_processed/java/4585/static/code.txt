@PublicEvolving
	public static <T, C> ObjectArrayTypeInfo<T, C> getInfoFor(Class<T> arrayClass, TypeInformation<C> componentInfo) {
		checkNotNull(arrayClass);
		checkNotNull(componentInfo);
		checkArgument(arrayClass.isArray(), "Class " + arrayClass + " must be an array.");

		return new ObjectArrayTypeInfo<T, C>(arrayClass, componentInfo);
	}