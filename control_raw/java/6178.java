public Future<Path> createTmpFile(String name, DistributedCacheEntry entry, JobID jobID, ExecutionAttemptID executionId) throws Exception {
		synchronized (lock) {
			Map<String, Future<Path>> jobEntries = entries.computeIfAbsent(jobID, k -> new HashMap<>());

			// register reference holder
			final Set<ExecutionAttemptID> refHolders = jobRefHolders.computeIfAbsent(jobID, id -> new HashSet<>());
			refHolders.add(executionId);

			Future<Path> fileEntry = jobEntries.get(name);
			if (fileEntry != null) {
				// file is already in the cache. return a future that
				// immediately returns the file
				return fileEntry;
			} else {
				// need to copy the file

				// create the target path
				File tempDirToUse = new File(storageDirectories[nextDirectory++], jobID.toString());
				if (nextDirectory >= storageDirectories.length) {
					nextDirectory = 0;
				}

				// kick off the copying
				Callable<Path> cp;
				if (entry.blobKey != null) {
					cp = new CopyFromBlobProcess(entry, jobID, blobService, new Path(tempDirToUse.getAbsolutePath()));
				} else {
					cp = new CopyFromDFSProcess(entry, new Path(tempDirToUse.getAbsolutePath()));
				}
				FutureTask<Path> copyTask = new FutureTask<>(cp);
				executorService.submit(copyTask);

				// store our entry
				jobEntries.put(name, copyTask);

				return copyTask;
			}
		}
	}