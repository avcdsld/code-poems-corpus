private void initConnecton() {
		this.httpConnection = HttpConnection.create(URLUtil.toUrlForHttp(this.url, this.urlHandler), this.proxy)//
				.setMethod(this.method)//
				.setHttpsInfo(this.hostnameVerifier, this.ssf)//
				.setConnectTimeout(this.connectionTimeout)//
				.setReadTimeout(this.readTimeout)//
				// 自定义Cookie
				.setCookie(this.cookie)
				// 定义转发
				.setInstanceFollowRedirects(this.maxRedirectCount > 0 ? true : false)
				// 覆盖默认Header
				.header(this.headers, true);

		// 是否禁用缓存
		if (this.isDisableCache) {
			this.httpConnection.disableCache();
		}
	}