function getContentType(oResponse) {
	if (oResponse && oResponse.headers) {
		for (var sHeader in oResponse.headers) {
			if (sHeader.toLowerCase() === "content-type") {
				return oResponse.headers[sHeader].replace(/([^;]*);.*/, "$1");
			}
		}
	}
	return false;
}