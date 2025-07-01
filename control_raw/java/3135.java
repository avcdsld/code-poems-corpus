static Tuple2<Path, LocalResource> setupLocalResource(
		FileSystem fs,
		String appId,
		Path localSrcPath,
		Path homedir,
		String relativeTargetPath) throws IOException {

		File localFile = new File(localSrcPath.toUri().getPath());
		if (localFile.isDirectory()) {
			throw new IllegalArgumentException("File to copy must not be a directory: " +
				localSrcPath);
		}

		// copy resource to HDFS
		String suffix =
			".flink/"
				+ appId
				+ (relativeTargetPath.isEmpty() ? "" : "/" + relativeTargetPath)
				+ "/" + localSrcPath.getName();

		Path dst = new Path(homedir, suffix);

		LOG.debug("Copying from {} to {}", localSrcPath, dst);

		fs.copyFromLocalFile(false, true, localSrcPath, dst);

		// Note: If we used registerLocalResource(FileSystem, Path) here, we would access the remote
		//       file once again which has problems with eventually consistent read-after-write file
		//       systems. Instead, we decide to preserve the modification time at the remote
		//       location because this and the size of the resource will be checked by YARN based on
		//       the values we provide to #registerLocalResource() below.
		fs.setTimes(dst, localFile.lastModified(), -1);
		// now create the resource instance
		LocalResource resource = registerLocalResource(dst, localFile.length(), localFile.lastModified());

		return Tuple2.of(dst, resource);
	}