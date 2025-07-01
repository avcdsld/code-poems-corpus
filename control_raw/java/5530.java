public void mergeWith(OptionalBoolean other) {
		if (state == other.state) {
			// no change in state
		} else if (state == State.UNSET) {
			state = other.state;
		} else if (other.state == State.UNSET) {
			// no change in state
		} else {
			state = State.CONFLICTING;
		}
	}