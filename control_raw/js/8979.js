function missingValue(oValue, sSegment, iPathLength) {
			var sPropertyPath = "",
				sReadLink,
				sServiceUrl;

			if (sPath[0] !== '(') {
				sPropertyPath += "/";
			}
			sPropertyPath += sPath.split("/").slice(0, iPathLength).join("/");
			return that.oRequestor.getModelInterface()
				.fetchMetadata(that.sMetaPath + _Helper.getMetaPath(sPropertyPath))
				.then(function (oProperty) {
					if (!oProperty) {
						return invalidSegment(sSegment);
					}
					if (oProperty.$Type === "Edm.Stream") {
						sReadLink = oValue[sSegment + "@odata.mediaReadLink"];
						sServiceUrl = that.oRequestor.getServiceUrl();
						return sReadLink || sServiceUrl + that.sResourcePath + sPropertyPath;
					}
					if (!bTransient) {
						return invalidSegment(sSegment);
					}
					if (oProperty.$kind === "NavigationProperty") {
						return null;
					}
					if (!oProperty.$Type.startsWith("Edm.")) {
						return {};
					}
					if ("$DefaultValue" in oProperty) {
						return oProperty.$Type === "Edm.String"
							? oProperty.$DefaultValue
							: _Helper.parseLiteral(oProperty.$DefaultValue, oProperty.$Type,
								sPropertyPath);
					}
					return null;
				});
		}