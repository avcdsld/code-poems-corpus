@SuppressWarnings({ "unchecked", "rawtypes" })
	@Override
	public T reduce(T value1, T value2) throws Exception {

		for (int position : fields) {
			// Save position of compared key
			// Get both values - both implement comparable
			Comparable comparable1 = value1.getFieldNotNull(position);
			Comparable comparable2 = value2.getFieldNotNull(position);

			// Compare values
			int comp = comparable1.compareTo(comparable2);
			// If comp is smaller than 0 comparable 1 is smaller.
			// Return the smaller value.
			if (comp < 0) {
				return value1;
			} else if (comp > 0) {
				return value2;
			}
		}
		return value1;
	}