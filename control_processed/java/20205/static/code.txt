public <E> void setComboBoxModel(String fieldLabel, ComboBoxModel<E> comboBoxModel) {
		Component c = this.fieldMap.get(fieldLabel);
		if (c instanceof JComboBox) {
			@SuppressWarnings("unchecked")
			JComboBox<E> comboBox = (JComboBox<E>) c;
			comboBox.setModel(comboBoxModel);
		} else if (c == null) {
			// Ignore - could be during init
			logger.debug("No field for " + fieldLabel);
		} else {
			handleUnexpectedFieldClass(fieldLabel, c);
		}
	}