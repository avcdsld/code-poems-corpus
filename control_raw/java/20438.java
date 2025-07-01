public void hideColumn(TableColumn column) {
		if (columnModel.getColumnCount() == 1) {
			return;
		}

		// Ignore changes to the TableColumnModel made by the TableColumnManager

		columnModel.removeColumnModelListener(this);
		columnModel.removeColumn(column);
		columnModel.addColumnModelListener(this);
	}