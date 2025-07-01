public final void setUndoManagerPolicy(UndoManagerPolicy policy) throws NullPointerException {
		if (policy == null) {
			throw new NullPointerException("The policy must not be null.");
		}
		
		if (this.policy == policy) {
			return;
		}

		final UndoManagerPolicy oldPolicy = this.policy;
		this.policy = policy;
		
		if (oldPolicy == UndoManagerPolicy.DEFAULT) {
			this.textComponent.removePropertyChangeListener("editable", this);
			this.textComponent.removePropertyChangeListener("enabled", this);
		}

		if (this.policy == UndoManagerPolicy.DEFAULT) {
			this.textComponent.addPropertyChangeListener("editable", this);
			this.textComponent.addPropertyChangeListener("enabled", this);
		}

		handleUndoManagerPolicy();
	}