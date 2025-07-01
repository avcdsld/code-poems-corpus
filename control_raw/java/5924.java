public static OutputStreamAndPath createEntropyAware(
			FileSystem fs,
			Path path,
			WriteMode writeMode) throws IOException {

		// check and possibly inject entropy into the path
		final EntropyInjectingFileSystem efs = getEntropyFs(fs);
		final Path processedPath = efs == null ? path : resolveEntropy(path, efs, true);

		// create the stream on the original file system to let the safety net
		// take its effect
		final FSDataOutputStream out = fs.create(processedPath, writeMode);
		return new OutputStreamAndPath(out, processedPath);
	}