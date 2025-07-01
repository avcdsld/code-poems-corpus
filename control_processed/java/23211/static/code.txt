public static <T> List<T> disjoint(final List<? extends T> list1, final List<? extends T> list2) {
		List<T> intersection = intersection(list1, list2);
		List<T> towIntersection = union(intersection, intersection);
		return difference(union(list1, list2), towIntersection);
	}