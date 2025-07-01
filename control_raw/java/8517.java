public FileAppender append(String line) {
		if (list.size() >= capacity) {
			flush();
		}
		list.add(line);
		return this;
	}