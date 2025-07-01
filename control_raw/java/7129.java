public static byte[] gzip(InputStream in, int length) throws UtilException {
		final ByteArrayOutputStream bos = new ByteArrayOutputStream(length);
		GZIPOutputStream gos = null;
		try {
			gos = new GZIPOutputStream(bos);
			IoUtil.copy(in, gos);
		} catch (IOException e) {
			throw new UtilException(e);
		} finally {
			IoUtil.close(gos);
		}
		//返回必须在关闭gos后进行，因为关闭时会自动执行finish()方法，保证数据全部写出
		return bos.toByteArray();
	}