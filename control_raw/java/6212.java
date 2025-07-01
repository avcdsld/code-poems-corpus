public void close() throws IOException {
		
		// we go on closing and deleting files in the presence of failures.
		// we remember the first exception to occur and re-throw it later
		Throwable ex = null;
		
		synchronized (this) {
			
			if (closed) {
				return;
			}
			closed = true;
			
			// close the writers
			if (recordsOutFile != null) {
				try {
					recordsOutFile.close();
					recordsOutFile = null;
				} catch (Throwable t) {
					LOG.error("Cannot close the large records spill file.", t);
					ex = ex == null ? t : ex;
				}
			}
			if (keysOutFile != null) {
				try {
					keysOutFile.close();
					keysOutFile = null;
				} catch (Throwable t) {
					LOG.error("Cannot close the large records key spill file.", t);
					ex = ex == null ? t : ex;
				}
			}
			
			// close the readers
			if (recordsReader != null) {
				try {
					recordsReader.close();
					recordsReader = null;
				} catch (Throwable t) {
					LOG.error("Cannot close the large records reader.", t);
					ex = ex == null ? t : ex;
				}
			}
			if (keysReader != null) {
				try {
					keysReader.close();
					keysReader = null;
				} catch (Throwable t) {
					LOG.error("Cannot close the large records key reader.", t);
					ex = ex == null ? t : ex;
				}
			}
			
			// delete the spill files
			if (recordsChannel != null) {
				try {
					ioManager.deleteChannel(recordsChannel);
					recordsChannel = null;
				} catch (Throwable t) {
					LOG.error("Cannot delete the large records spill file.", t);
					ex = ex == null ? t : ex;
				}
			}
			if (keysChannel != null) {
				try {
					ioManager.deleteChannel(keysChannel);
					keysChannel = null;
				} catch (Throwable t) {
					LOG.error("Cannot delete the large records key spill file.", t);
					ex = ex == null ? t : ex;
				}
			}
			
			// close the key sorter
			if (keySorter != null) {
				try {
					keySorter.close();
					keySorter = null;
				} catch (Throwable t) {
					LOG.error("Cannot properly dispose the key sorter and clean up its temporary files.", t);
					ex = ex == null ? t : ex;
				}
			}
			
			memManager.release(memory);
			
			recordCounter = 0;
		}
		
		// re-throw the exception, if necessary
		if (ex != null) { 
			throw new IOException("An error occurred cleaning up spill files in the large record handler.", ex);
		}
	}