public static void copy(final File sourceFile, File targetFile, final boolean overwrite) throws IOException {
        if (sourceFile == null) {
            throw new IOException("Source must not be null");
        }

        if (targetFile == null) {
            throw new IOException("Target must not be null");
        }

        // checks
        if ((false == sourceFile.isFile()) || (false == sourceFile.exists())) {
            throw new IOException("Source file '" + sourceFile.getAbsolutePath() + "' not found!");
        }

        if (true == targetFile.exists()) {
            if (true == targetFile.isDirectory()) {

                // Directory? -> use source file name
                targetFile = new File(targetFile, sourceFile.getName());
            } else if (true == targetFile.isFile()) {
                if (false == overwrite) {
                    throw new IOException("Target file '" + targetFile.getAbsolutePath() + "' already exists!");
                }
            } else {
                throw new IOException("Invalid target object '" + targetFile.getAbsolutePath() + "'!");
            }
        } else {
            // create parent dir
            FileUtils.forceMkdir(targetFile.getParentFile());
        }

        FileInputStream input = null;
        FileOutputStream output = null;

        try {
            input = new FileInputStream(sourceFile);
            output = new FileOutputStream(targetFile);
            copy(input, output);
            output.flush();
        } finally {
            IOUtils.closeQuietly(input);
            IOUtils.closeQuietly(output);
        }
    }