function (sServiceUrl, oModelInterface, mHeaders, mQueryParams, sODataVersion) {
			var oRequestor = new Requestor(sServiceUrl, mHeaders, mQueryParams, oModelInterface);

			if (sODataVersion === "2.0") {
				asV2Requestor(oRequestor);
			}

			return oRequestor;
		}