public static void writeFileInfoToConfig(String name, DistributedCacheEntry e, Configuration conf) {
		int num = conf.getInteger(CACHE_FILE_NUM, 0) + 1;
		conf.setInteger(CACHE_FILE_NUM, num);
		conf.setString(CACHE_FILE_NAME + num, name);
		conf.setString(CACHE_FILE_PATH + num, e.filePath);
		conf.setBoolean(CACHE_FILE_EXE + num, e.isExecutable || new File(e.filePath).canExecute());
		conf.setBoolean(CACHE_FILE_DIR + num, e.isZipped || new File(e.filePath).isDirectory());
		if (e.blobKey != null) {
			conf.setBytes(CACHE_FILE_BLOB_KEY + num, e.blobKey);
		}
	}