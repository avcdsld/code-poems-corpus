private void checkIdentity(SSLSession session, X509Certificate cert) throws CertificateException {
		if (session == null) {
			throw new CertificateException("No handshake session");
		}

		if (EndpointIdentificationAlgorithm.HTTPS == identityAlg) {
			String hostname = session.getPeerHost();
			APINameChecker.verifyAndThrow(hostname, cert);
		}
	}