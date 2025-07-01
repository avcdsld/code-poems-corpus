public <S extends F> Pattern<T, S> subtype(final Class<S> subtypeClass) {
		Preconditions.checkNotNull(subtypeClass, "The class cannot be null.");

		if (condition == null) {
			this.condition = new SubtypeCondition<F>(subtypeClass);
		} else {
			this.condition = new RichAndCondition<>(condition, new SubtypeCondition<F>(subtypeClass));
		}

		@SuppressWarnings("unchecked")
		Pattern<T, S> result = (Pattern<T, S>) this;

		return result;
	}