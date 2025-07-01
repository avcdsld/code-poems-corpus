public void printToErr() throws Exception {
		List<T> elements = collect();
		for (T e: elements) {
			System.err.println(e);
		}
	}