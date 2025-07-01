function() {

									// Prerequisite: sap-context-token must not be set in the model URI
									if (oUri.hasQuery("sap-context-token")) {
										Log.warning("Component Manifest: Ignoring provided \"sap-context-token=" + sCacheToken + "\" for model \"" + sModelName + "\" (" + oUri.toString() + "). " +
											"Model URI already contains parameter \"sap-context-token=" + oUri.query(true)["sap-context-token"] + "\"",
											"[\"sap.ui5\"][\"models\"][\"" + sModelName + "\"]", sLogComponentName);
										return;
									}

									// 1. "sap-language" must be set in "oModelConfig.settings.metadataUrlParams"
									// or part of the model URI
									if ((!mMetadataUrlParams || typeof mMetadataUrlParams["sap-language"] === "undefined")
										&& !oUri.hasQuery("sap-language")
									) {
										Log.warning("Component Manifest: Ignoring provided \"sap-context-token=" + sCacheToken + "\" for model \"" + sModelName + "\" (" + oUri.toString() + "). " +
											"Missing \"sap-language\" parameter",
											"[\"sap.ui5\"][\"models\"][\"" + sModelName + "\"]", sLogComponentName);
										return;
									}

									// 2. "sap-client" must be set as URI param in "oModelConfig.uri"
									if (!oUri.hasQuery("sap-client")) {
										Log.warning("Component Manifest: Ignoring provided \"sap-context-token=" + sCacheToken + "\" for model \"" + sModelName + "\" (" + oUri.toString() + "). " +
											"Missing \"sap-client\" parameter",
											"[\"sap.ui5\"][\"models\"][\"" + sModelName + "\"]", sLogComponentName);
										return;
									}

									// 3. "sap-client" must equal to the value of "sap.ui.getCore().getConfiguration().getSAPParam('sap-client')"
									if (!oUri.hasQuery("sap-client", oConfig.getSAPParam("sap-client"))) {
										Log.warning("Component Manifest: Ignoring provided \"sap-context-token=" + sCacheToken + "\" for model \"" + sModelName + "\" (" + oUri.toString() + "). " +
											"URI parameter \"sap-client=" + oUri.query(true)["sap-client"] + "\" must be identical with configuration \"sap-client=" + oConfig.getSAPParam("sap-client") + "\"",
											"[\"sap.ui5\"][\"models\"][\"" + sModelName + "\"]", sLogComponentName);
										return;
									}

									// 4. If "mMetadataUrlParams["sap-client"]" is set (which should not be done!), it must also equal to the value of the config
									if (mMetadataUrlParams && typeof mMetadataUrlParams["sap-client"] !== "undefined") {
										if (mMetadataUrlParams["sap-client"] !== oConfig.getSAPParam("sap-client")) {
											Log.warning("Component Manifest: Ignoring provided \"sap-context-token=" + sCacheToken + "\" for model \"" + sModelName + "\" (" + oUri.toString() + "). " +
												"Parameter metadataUrlParams[\"sap-client\"] = \"" + mMetadataUrlParams["sap-client"] + "\" must be identical with configuration \"sap-client=" + oConfig.getSAPParam("sap-client") + "\"",
												"[\"sap.ui5\"][\"models\"][\"" + sModelName + "\"]", sLogComponentName);
											return;
										}
									}

									// Overriding the parameter is fine as the given one should be the most up-to-date
									if (mMetadataUrlParams && mMetadataUrlParams["sap-context-token"] && mMetadataUrlParams["sap-context-token"] !== sCacheToken) {
										Log.warning("Component Manifest: Overriding existing \"sap-context-token=" + mMetadataUrlParams["sap-context-token"] + "\" with provided value \"" + sCacheToken + "\" for model \"" + sModelName + "\" (" + oUri.toString() + ").",
											"[\"sap.ui5\"][\"models\"][\"" + sModelName + "\"]", sLogComponentName);
									}

									// Lazy initialize settings and metadataUrlParams objects
									if (!mMetadataUrlParams) {
										oModelConfig.settings = oModelConfig.settings || {};
										mMetadataUrlParams = oModelConfig.settings.metadataUrlParams = oModelConfig.settings.metadataUrlParams || {};
									}

									// Finally, set the sap-context-token
									mMetadataUrlParams["sap-context-token"] = sCacheToken;

								}