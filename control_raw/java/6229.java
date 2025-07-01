@Override
	public boolean remove(@Nonnull T toRemove) {
		T storedElement = getDedupMapForElement(toRemove).remove(toRemove);
		return storedElement != null && super.remove(storedElement);
	}