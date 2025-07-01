public void setFields(String[] requiredFields, String[] optionalFields) {
		if (requiredFields == null) {
			throw new IllegalArgumentException("Parameter requiredFields must not be null.");
		}

		if (optionalFields == null) {
			throw new IllegalArgumentException("Parameter optionalFields must not be null.");
		}

		this.requiredFields = requiredFields;
		this.optionalFields = optionalFields;

		this.textFields = new HashMap<>(requiredFields.length + optionalFields.length);

		removeAll();

		int fieldIndex = 0;
		for (String fieldName : requiredFields) {
			addRequiredField(fieldName, fieldIndex);
			fieldIndex++;
		}

		for (String fieldName : optionalFields) {
			addField(fieldName, fieldIndex);
			fieldIndex++;
		}
		add(Box.createVerticalGlue(), LayoutHelper.getGBC(0, fieldIndex, 2, 0.0d, 1.0d));

		validate();
	}