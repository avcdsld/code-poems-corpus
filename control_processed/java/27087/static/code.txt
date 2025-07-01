public static String hmacSHA256(String stringSignTemp, String partnerKey)  throws UnsupportedEncodingException, NoSuchAlgorithmException, InvalidKeyException {
		Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
		SecretKeySpec secret_key = new SecretKeySpec(partnerKey.getBytes(), "HmacSHA256");
		sha256_HMAC.init(secret_key);
		return byteArrayToHexString(sha256_HMAC.doFinal(stringSignTemp.getBytes("utf-8")));
	}