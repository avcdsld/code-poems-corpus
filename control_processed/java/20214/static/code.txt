public void setFieldPopupMenu(String fieldLabel, JPopupMenu popup) {
		Component c = this.fieldMap.get(fieldLabel);
		if (c != null) {
			if (c instanceof JComponent) {
				((JComponent) c).setComponentPopupMenu(popup);
			} else {
				handleUnexpectedFieldClass(fieldLabel, c);
			}
		}
	}