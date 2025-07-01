function (oManifest) {
			if (oManifest) {
				if (oManifest.getEntry("sap.ui5")) {
					if (oManifest.getEntry("sap.ui5").appVariantId) {
						return oManifest.getEntry("sap.ui5").appVariantId;
					}
					if (oManifest.getEntry("sap.ui5").componentName) {
					    var sComponentName = oManifest.getEntry("sap.ui5").componentName;
					    if (sComponentName.length > 0 && sComponentName.indexOf(".Component") < 0) {
						sComponentName += ".Component";
					    }
					    return sComponentName;
					}
				}
				if (oManifest.getEntry("sap.app") && oManifest.getEntry("sap.app").id) {
					var sAppId = oManifest.getEntry("sap.app").id;
					if (sAppId === Utils.APP_ID_AT_DESIGN_TIME && oManifest.getComponentName) {
					    sAppId = oManifest.getComponentName();
					}
					if (sAppId.length > 0 && sAppId.indexOf(".Component") < 0) {
					    sAppId += ".Component";
					}
					return sAppId;
				}
			}
			this.log.warning("No Manifest received.");
			return "";
		}