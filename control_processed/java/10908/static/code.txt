private void rename(File legacyFile, File newFile) throws IOException {
        if (!legacyFile.exists())   return;
        if (newFile.exists()) {
            Util.deleteFile(newFile);
        }
        if (!legacyFile.renameTo(newFile)) {
            LOGGER.warning("Failed to rename " + legacyFile + " to " + newFile);
        }
    }