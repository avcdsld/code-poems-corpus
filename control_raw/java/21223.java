protected void copySessionDb(String currentFile, String destFile) throws Exception {

		// ZAP: Changed to call the method close(boolean, boolean).
		getDb().close(false, false);

		// copy session related files to the path specified
		FileCopier copier = new FileCopier();

		// ZAP: Check if files exist.
		File fileIn1 = new File(currentFile + ".data");
		if (fileIn1.exists()) {
			File fileOut1 = new File(destFile + ".data");
			copier.copy(fileIn1, fileOut1);
		}

		File fileIn2 = new File(currentFile + ".script");
		if (fileIn2.exists()) {
			File fileOut2 = new File(destFile + ".script");
			copier.copy(fileIn2, fileOut2);
		}

		File fileIn3 = new File(currentFile + ".properties");
		if (fileIn3.exists()) {
			File fileOut3 = new File(destFile + ".properties");
			copier.copy(fileIn3, fileOut3);
		}

		File fileIn4 = new File(currentFile + ".backup");
		if (fileIn4.exists()) {
			File fileOut4 = new File(destFile + ".backup");
			copier.copy(fileIn4, fileOut4);
		}

		// ZAP: Handle the "lobs" file.
		File lobsFile = new File(currentFile + ".lobs");
		if (lobsFile.exists()) {
			File newLobsFile = new File(destFile + ".lobs");
			copier.copy(lobsFile, newLobsFile);
		}

		getDb().open(destFile);

	}