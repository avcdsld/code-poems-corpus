function(sBaseUrl, oSyncPoint) {

		// determine the index
		var mIndex = oSession.index;

		// the request object
		var oRequest;
		var sUrl;
		var sAbsoluteBaseUrl;

		// in case of an incoming array we register each base url on its own
		// except in case of the batch mode => there we pass all URLs in a POST request.
		if (Array.isArray(sBaseUrl) && !bBatch) {

			sBaseUrl.forEach(function(sBaseUrlEntry) {
				fnRegister(sBaseUrlEntry, oSyncPoint);
			});

		} else if (Array.isArray(sBaseUrl) && bBatch) {

			// BATCH MODE: send all base urls via POST request to the server
			//   -> server returns a JSON object for containing the index for
			//      different base urls.
			//
			// returns e.g.:
			// {
			//    "<absolute_url>": { ...<index>... },
			//    ...
			// }
			var sRootUrl = fnEnsureTrailingSlash(sBaseUrl[0]);
			var sContent = [];

			// log
			Log.debug("sap.ui.core.AppCacheBuster.register(\"" + sRootUrl + "\"); // BATCH MODE!");

			// determine the base URL
			var sAbsoluteRootUrl = AppCacheBuster.normalizeURL(sRootUrl); // "./" removes the html doc from path

			// log
			Log.debug("  --> normalized to: \"" + sAbsoluteRootUrl + "\"");

			// create the list of absolute base urls
			sBaseUrl.forEach(function(sUrlEntry) {
				sUrl = fnEnsureTrailingSlash(sUrlEntry);
				var sAbsoluteUrl = AppCacheBuster.normalizeURL(sUrl);
				if (!mIndex[sAbsoluteBaseUrl]) {
					sContent.push(sAbsoluteUrl);
				}
			});

			// if we need to fetch some base urls we trigger the request otherwise
			// we gracefully ignore the function call
			if (sContent.length > 0) {

				// create the URL for the index file
				var sUrl = sAbsoluteRootUrl + "sap-ui-cachebuster-info.json?sap-ui-language=" + sLanguage;

				// configure request; check how to execute the request (sync|async)
				oRequest = {
						url: sUrl,
						type: "POST",
						async: !bSync && !!oSyncPoint,
						dataType: "json",
						contentType: "text/plain",
						data: sContent.join("\n"),
						success: function(data) {
							// notify that the content has been loaded
							AppCacheBuster.onIndexLoaded(sUrl, data);
							// add the index file to the index map
							jQuery.extend(mIndex, data);
						},
						error: function() {
							Log.error("Failed to batch load AppCacheBuster index file from: \"" + sUrl + "\".");
						}
				};

			}

		} else {

			// ensure the trailing slash
			sBaseUrl = fnEnsureTrailingSlash(sBaseUrl);

			// log
			Log.debug("sap.ui.core.AppCacheBuster.register(\"" + sBaseUrl + "\");");

			// determine the base URL
			sAbsoluteBaseUrl = AppCacheBuster.normalizeURL(sBaseUrl); // "./" removes the html doc from path

			// log
			Log.debug("  --> normalized to: \"" + sAbsoluteBaseUrl + "\"");

			// if the index file has not been loaded yet => load!
			if (!mIndex[sAbsoluteBaseUrl]) {

				// create the URL for the index file
				var sUrl = sAbsoluteBaseUrl + "sap-ui-cachebuster-info.json?sap-ui-language=" + sLanguage;

				// configure request; check how to execute the request (sync|async)
				oRequest = {
						url: sUrl,
						async: !bSync && !!oSyncPoint,
						dataType: "json",
						success: function(data) {
							// notify that the content has been loaded
							AppCacheBuster.onIndexLoaded(sUrl, data);
							// add the index file to the index map
							mIndex[sAbsoluteBaseUrl] = data;
						},
						error: function() {
							Log.error("Failed to load AppCacheBuster index file from: \"" + sUrl + "\".");
						}
				};

			}

		}

		// only request in case of having a correct request object!
		if (oRequest) {

			// hook to onIndexLoad to allow to inject the index file manually
			var mIndexInfo = AppCacheBuster.onIndexLoad(oRequest.url);
			// if anything else than undefined or null is returned we will use this
			// content as data for the cache buster index
			if (mIndexInfo != null) {
				Log.info("AppCacheBuster index file injected for: \"" + sUrl + "\".");
				oRequest.success(mIndexInfo);
			} else {

				// use the syncpoint only during boot => otherwise the syncpoint
				// is not given because during runtime the registration needs to
				// be done synchronously.
				if (oRequest.async) {
					var iSyncPoint = oSyncPoint.startTask("load " + sUrl);
					var fnSuccess = oRequest.success, fnError = oRequest.error;
					jQuery.extend(oRequest, {
						success: function(data) {
							fnSuccess.apply(this, arguments);
							oSyncPoint.finishTask(iSyncPoint);
						},
						error: function() {
							fnError.apply(this, arguments);
							oSyncPoint.finishTask(iSyncPoint, false);
						}
					});
				}

				// load it
				Log.info("Loading AppCacheBuster index file from: \"" + sUrl + "\".");
				jQuery.ajax(oRequest);

			}

		}

	}