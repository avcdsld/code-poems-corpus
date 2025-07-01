function setupDialog() {
				// setup e2e values as log level and content
				if (dialog.traceXml) {
					dialog.$(e2eTraceConst.taContent).text(dialog.traceXml);
				}
				if (dialog.e2eLogLevel) {
					dialog.$(e2eTraceConst.selLevel).val(dialog.e2eLogLevel);
				}

				fillPanelContent(controlIDs.dvLoadedModules, oData.modules);


				// bind button Start event
				dialog.$(e2eTraceConst.btnStart).one("tap", function () {

					dialog.e2eLogLevel = dialog.$(e2eTraceConst.selLevel).val();
					dialog.$(e2eTraceConst.btnStart).addClass("sapUiSupportRunningTrace").text("Running...");
					dialog.traceXml = "";
					dialog.$(e2eTraceConst.taContent).text("");

					sap.ui.core.support.trace.E2eTraceLib.start(dialog.e2eLogLevel, function (traceXml) {
						dialog.traceXml = traceXml;
					});

					// show info message about the E2E trace activation
					sap.m.MessageToast.show(e2eTraceConst.infoText, {duration: e2eTraceConst.infoDuration});

					//close the dialog, but keep it for later use
					dialog.close();
				});
			}