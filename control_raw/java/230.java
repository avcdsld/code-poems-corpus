static <T> T doWithMainClasses(File rootFolder, MainClassCallback<T> callback)
			throws IOException {
		if (!rootFolder.exists()) {
			return null; // nothing to do
		}
		if (!rootFolder.isDirectory()) {
			throw new IllegalArgumentException(
					"Invalid root folder '" + rootFolder + "'");
		}
		String prefix = rootFolder.getAbsolutePath() + "/";
		Deque<File> stack = new ArrayDeque<>();
		stack.push(rootFolder);
		while (!stack.isEmpty()) {
			File file = stack.pop();
			if (file.isFile()) {
				try (InputStream inputStream = new FileInputStream(file)) {
					ClassDescriptor classDescriptor = createClassDescriptor(inputStream);
					if (classDescriptor != null && classDescriptor.isMainMethodFound()) {
						String className = convertToClassName(file.getAbsolutePath(),
								prefix);
						T result = callback.doWith(new MainClass(className,
								classDescriptor.getAnnotationNames()));
						if (result != null) {
							return result;
						}
					}
				}
			}
			if (file.isDirectory()) {
				pushAllSorted(stack, file.listFiles(PACKAGE_FOLDER_FILTER));
				pushAllSorted(stack, file.listFiles(CLASS_FILE_FILTER));
			}
		}
		return null;
	}