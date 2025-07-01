public byte[] digest(File file) throws CryptoException{
		InputStream in = null;
		try {
			in = FileUtil.getInputStream(file);
			return digest(in);
		} finally{
			IoUtil.close(in);
		}
	}