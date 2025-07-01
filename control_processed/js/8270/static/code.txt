function () {
                // ##### END: MODIFIED BY SAP
                    if (done || xhr === null || xhr.readyState !== 4) {
                        return;
                    }

                    // Workaround for XHR behavior on IE.
                    var statusText = xhr.statusText;
                    var statusCode = xhr.status;
                    if (statusCode === 1223) {
                        statusCode = 204;
                        statusText = "No Content";
                    }

                    var headers = [];
                    readResponseHeaders(xhr, headers);

                    // ##### BEGIN: MODIFIED BY SAP
                    var xml = null;
                    if (datajs._sap && xhr.responseXML) {
                    	xml = xhr.responseXML;
                    }
                   	// ##### END: MODIFIED BY SAP

                    var response = { requestUri: url, statusCode: statusCode, statusText: statusText, headers: headers, body: xhr.responseText };

                    done = true;
                    xhr = null;
                    if (statusCode >= 200 && statusCode <= 299) {
                        success(response);
                    } else {
                    	// ##### BEGIN: MODIFIED BY SAP
                    	// normalize response headers here which is also done in the success function call above
                      	normalizeHeaders(response.headers);
                      	// ##### END: MODIFIED BY SAP
                        error({ message: "HTTP request failed", request: request, response: response });
                    }
                    // ##### BEGIN: MODIFIED BY SAP
                    if (datajs._sap && response.requestUri.indexOf("$metadata") > -1) {

                    	var mSettings = {
                      	   supportXML: xml,
                      	   response: response
                      	};
                    	datajs._sap._supportInfo({context: xml, env: {caller:'datajs', settings: mSettings, type:"metadata"}});
                    }
                    // ##### END: MODIFIED BY SAP
                }