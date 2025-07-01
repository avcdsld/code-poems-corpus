protected void cleanFile(String path) {
		try {
			PrintWriter writer;
			writer = new PrintWriter(path);
			writer.print("");
			writer.close();
		} catch (FileNotFoundException e) {
			throw new RuntimeException("An error occurred while cleaning the file: " + e.getMessage(), e);
		}
	}