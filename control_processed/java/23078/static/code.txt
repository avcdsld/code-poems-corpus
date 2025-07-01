public static void moveFile(@NotNull Path from, @NotNull Path to) throws IOException {
		Validate.isTrue(isFileExists(from), "%s is not exist or not a file", from);
		Validate.notNull(to);
		Validate.isTrue(!isDirExists(to), "%s is  exist but it is a dir", to);

		Files.move(from, to);
	}