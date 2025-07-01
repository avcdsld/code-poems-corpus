public byte[] decrypt(String data, KeyType keyType) {
		return decrypt(SecureUtil.decode(data), keyType);
	}