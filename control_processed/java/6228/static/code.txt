@Override
	public boolean add(@Nonnull T element) {
		return getDedupMapForElement(element).putIfAbsent(element, element) == null && super.add(element);
	}