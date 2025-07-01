public static String encode(String url, String charset) throws UtilException {
		if (StrUtil.isEmpty(url)) {
			return url;
		}
		return encode(url, StrUtil.isBlank(charset) ? CharsetUtil.defaultCharset() : CharsetUtil.charset(charset));
	}