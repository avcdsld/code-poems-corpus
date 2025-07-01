public int getIndexOf(Object object) {
		int index = tableModel.getUsers().indexOf(object);
		if (index < 0 && customUsers != null)
			return tableModel.getUsers().size() + ArrayUtils.indexOf(customUsers, object);
		return index;
	}