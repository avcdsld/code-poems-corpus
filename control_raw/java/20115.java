@Override
	public void close(boolean compact, boolean cleanup) {
		// ZAP: Added statement.
		logger.debug("close");
	    if (databaseServer == null) {
	    	return;
	    }

	    super.close(compact, cleanup);
	    
	    try {
	        // ZAP: Added if block.
	        if (cleanup) {
    		    // perform clean up
    	        getTableHistory().deleteTemporary();
	        }
        } catch (Exception e) {
	        // ZAP: Changed to log the exception.
            logger.error(e.getMessage(), e);
        }
	}