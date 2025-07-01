public static String encryptByPublicKey(String data, String publicKey) throws Exception {
		return encryptByPublicKey(data, publicKey, "RSA/ECB/PKCS1Padding");
	}