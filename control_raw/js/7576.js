function(sCodeRef, sViewId) {
					var oFlexSettings = oRta.getFlexSettings();
					if (!oFlexSettings.developerMode) {
						throw DtUtil.createError("service.ControllerExtension#add", "code extensions can only be created in developer mode", "sap.ui.rta");
					}

					if (!sCodeRef) {
						throw DtUtil.createError("service.ControllerExtension#add", "can't create controller extension without codeRef", "sap.ui.rta");
					}

					if (!sCodeRef.endsWith(".js")) {
						throw DtUtil.createError("service.ControllerExtension#add", "codeRef has to end with 'js'");
					}

					var oFlexController = oRta._getFlexController();
					var oView = sap.ui.getCore().byId(sViewId);
					var oAppComponent = FlexUtils.getAppComponentForControl(oView);
					var sControllerName = oView.getControllerName && oView.getControllerName() || oView.getController() && oView.getController().getMetadata().getName();

					var oChangeSpecificData = {
						content: {
							codeRef: sCodeRef
						},
						selector: {
							controllerName: sControllerName
						},
						changeType: "codeExt",
						namespace: oFlexSettings.namespace,
						developerMode: oFlexSettings.developerMode,
						scenario: oFlexSettings.scenario
					};

					var oPreparedChange = oFlexController.createBaseChange(oChangeSpecificData, oAppComponent);
					oFlexController.addPreparedChange(oPreparedChange, oAppComponent);
					return oPreparedChange.getDefinition();
				}