public String handleCallBack(HttpMessage msg)  throws ApiException {
		throw new ApiException (ApiException.Type.URL_NOT_FOUND, msg.getRequestHeader().getURI().toString());
	}