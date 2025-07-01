@SafeVarargs
	public static <T> List<T> sortPageAll(int pageNo, int pageSize, Comparator<T> comparator, Collection<T>... colls) {
		final List<T> list = new ArrayList<>(pageNo * pageSize);
		for (Collection<T> coll : colls) {
			list.addAll(coll);
		}
		if (null != comparator) {
			Collections.sort(list, comparator);
		}

		return page(pageNo, pageSize, list);
	}