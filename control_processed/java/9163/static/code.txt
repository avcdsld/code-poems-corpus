public static boolean verify(final String name, final X509Certificate cert) {
        try {
        	verifier.verify(name, cert);
            return true;
        } catch (final SSLException ex) {
        	// this is only logged here because eventually a CertificateException will be throw in verifyAndThrow.
        	// If this method is called in another method, the caller should be responsible to throw exceptions,
            logger.error(ex.getMessage(), ex);
            
            return false;
        }
    }