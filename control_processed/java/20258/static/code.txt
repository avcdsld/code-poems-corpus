public HttpMessage handleApiRequest (HttpRequestHeader requestHeader, HttpInputStream httpIn, 
			HttpOutputStream httpOut) throws IOException {
		return this.handleApiRequest(requestHeader, httpIn, httpOut, false);
	}