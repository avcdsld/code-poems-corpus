function matchHost(req, aUrl) {
	var thisServer = {
		host: req.headers.host
	};
	var parsedUrl = url.parse(aUrl);
	if (parsedUrl.host === thisServer.host) {
		parsedUrl.host = '';
		return url.format(parsedUrl);
	}
	return aUrl;
}