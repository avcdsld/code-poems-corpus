public void addContext(Context c) {
		if (c == null) {
			throw new IllegalArgumentException("The context must not be null. ");
		}
		validateContextName(c.getName());

		this.contexts.add(c);
		this.model.loadContext(c);

		for (OnContextsChangedListener l : contextsChangedListeners) {
			l.contextAdded(c);
		}
		
		if (View.isInitialised()) {
			View.getSingleton().addContext(c);
		}
	}