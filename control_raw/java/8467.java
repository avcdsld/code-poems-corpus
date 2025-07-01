public static KeyPair getKeyPair(String type, InputStream in, char[] password, String alias) {
		final KeyStore keyStore = readKeyStore(type, in, password);
		return getKeyPair(keyStore, password, alias);
	}