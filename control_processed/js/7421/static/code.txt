function(sServiceRootURI) {
			var sURI = null;
			if (this._sResourcePath != null) {
				sURI = (sServiceRootURI ? sServiceRootURI : "") + this._sResourcePath;
			} else if (this._oQueryResult.getParameterization()) {
				if (!this._oParameterizationRequest) {
					throw "Missing parameterization request";
				} else {
					sURI = this._oParameterizationRequest.getURIToParameterizationEntry(sServiceRootURI) + "/"
							+ this._oQueryResult.getParameterization().getNavigationPropertyToQueryResult();
				}
			} else {
				sURI = (sServiceRootURI ? sServiceRootURI : "") + "/" + this._oQueryResult.getEntitySet().getQName();
			}
			return sURI;
		}