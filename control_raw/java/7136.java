public static byte[] unZlib(InputStream in, int length) {
		final ByteArrayOutputStream out = new ByteArrayOutputStream(length);
		inflater(in, out);
		return out.toByteArray();
	}