public Digester init(String algorithm, Provider provider) {
		if(null == provider) {
			this.digest = SecureUtil.createMessageDigest(algorithm);
		}else {
			try {
				this.digest = MessageDigest.getInstance(algorithm, provider);
			} catch (NoSuchAlgorithmException e) {
				throw new CryptoException(e);
			}
		}
		return this;
	}