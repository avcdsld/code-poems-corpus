public static long downloadFile(String url, File destFile, int timeout, StreamProgress streamProgress) {
		if (StrUtil.isBlank(url)) {
			throw new NullPointerException("[url] is null!");
		}
		if (null == destFile) {
			throw new NullPointerException("[destFile] is null!");
		}
		final HttpResponse response = HttpRequest.get(url).timeout(timeout).executeAsync();
		if (false == response.isOk()) {
			throw new HttpException("Server response error with status code: [{}]", response.getStatus());
		}
		return response.writeBody(destFile, streamProgress);
	}