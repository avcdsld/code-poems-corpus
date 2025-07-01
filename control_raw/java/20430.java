@SuppressWarnings("unchecked")
	private JComboBox<HandleParametersOption> getComboHandleParameters() {
		if (handleParameters == null) {
			handleParameters = new JComboBox<>(new HandleParametersOption[] {
					HandleParametersOption.USE_ALL, HandleParametersOption.IGNORE_VALUE,
					HandleParametersOption.IGNORE_COMPLETELY });
			handleParameters.setRenderer(new HandleParametersOptionRenderer());
		}
		return handleParameters;
	}