static void skipSerializedStates(DataInputView in) throws IOException {
		TypeSerializer<String> nameSerializer = StringSerializer.INSTANCE;
		TypeSerializer<State.StateType> stateTypeSerializer = new EnumSerializer<>(State.StateType.class);
		TypeSerializer<StateTransitionAction> actionSerializer = new EnumSerializer<>(StateTransitionAction.class);

		final int noOfStates = in.readInt();

		for (int i = 0; i < noOfStates; i++) {
			nameSerializer.deserialize(in);
			stateTypeSerializer.deserialize(in);
		}

		for (int i = 0; i < noOfStates; i++) {
			String srcName = nameSerializer.deserialize(in);

			int noOfTransitions = in.readInt();
			for (int j = 0; j < noOfTransitions; j++) {
				String src = nameSerializer.deserialize(in);
				Preconditions.checkState(src.equals(srcName),
					"Source Edge names do not match (" + srcName + " - " + src + ").");

				nameSerializer.deserialize(in);
				actionSerializer.deserialize(in);

				try {
					skipCondition(in);
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			}
		}
	}