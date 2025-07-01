private HttpResponse init() throws HttpException {
		try {
			this.status = httpConnection.responseCode();
			this.in = (this.status < HttpStatus.HTTP_BAD_REQUEST) ? httpConnection.getInputStream() : httpConnection.getErrorStream();
		} catch (IOException e) {
			if (e instanceof FileNotFoundException) {
				// 服务器无返回内容，忽略之
			} else {
				throw new HttpException(e);
			}
		}

		try {
			this.headers = httpConnection.headers();
		} catch (IllegalArgumentException e) {
			StaticLog.warn(e, e.getMessage());
		}
		final Charset charset = httpConnection.getCharset();
		this.charsetFromResponse = charset;
		if (null != charset) {
			this.charset = charset;
		}

		if (null == this.in) {
			// 在一些情况下，返回的流为null，此时提供状态码说明
			this.in = new ByteArrayInputStream(StrUtil.format("Error request, response status: {}", this.status).getBytes());
		} else if (isGzip() && false == (in instanceof GZIPInputStream)) {
			try {
				in = new GZIPInputStream(in);
			} catch (IOException e) {
				// 在类似于Head等方法中无body返回，此时GZIPInputStream构造会出现错误，在此忽略此错误读取普通数据
				// ignore
			}
		} else if (isDeflate() && false == (in instanceof DeflaterInputStream)) {
			//Accept-Encoding: defalte
			in = new DeflaterInputStream(in);
		}

		// 同步情况下强制同步
		return this.isAsync ? this : forceSync();
	}