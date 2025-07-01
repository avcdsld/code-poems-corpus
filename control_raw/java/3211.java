@Override
	public void configure(Configuration parameters) {

		if (getFilePaths().length == 0) {
			// file path was not specified yet. Try to set it from the parameters.
			String filePath = parameters.getString(FILE_PARAMETER_KEY, null);
			if (filePath == null) {
				throw new IllegalArgumentException("File path was not specified in input format or configuration.");
			} else {
				setFilePath(filePath);
			}
		}

		if (!this.enumerateNestedFiles) {
			this.enumerateNestedFiles = parameters.getBoolean(ENUMERATE_NESTED_FILES_FLAG, false);
		}
	}