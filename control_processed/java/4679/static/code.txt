@Override
	public T next() {
		if (hasNext()) {
			T current = next;
			next = null;
			return current;
		} else {
			throw new NoSuchElementException();
		}
	}