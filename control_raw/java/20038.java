public Context getContext() {
		if (context == null) {
			context = Model.getSingleton().getSession().getContext(this.contextId);
		}
		return context;
	}