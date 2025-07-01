private void readBody(InputStream in) throws IORuntimeException {
		if (ignoreBody) {
			return;
		}

		int contentLength = Convert.toInt(header(Header.CONTENT_LENGTH), 0);
		final FastByteArrayOutputStream out = contentLength > 0 ? new FastByteArrayOutputStream(contentLength) : new FastByteArrayOutputStream();
		try {
			IoUtil.copy(in, out);
		} catch (IORuntimeException e) {
			if (e.getCause() instanceof EOFException || StrUtil.containsIgnoreCase(e.getMessage(), "Premature EOF")) {
				// 忽略读取HTTP流中的EOF错误
			} else {
				throw e;
			}
		}
		this.bodyBytes = out.toByteArray();
	}