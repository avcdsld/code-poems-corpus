function () {
			var that = this;
			var oSelectedContentModel = this.getView().getModel("selectedContent");
			var oContentData = oSelectedContentModel.getData();
			var sLayer;
			var sTransportIdFromContent, sPackageFromContent, sTransportId, sPackageName;
			oContentData.metadata.some(function (oMetadata) {
				if (oMetadata.name === "layer") {
					sLayer = oMetadata.value;
					return true;
				}
			});
			oContentData.metadata.some(function (mMetadata) {
				if (mMetadata.name === "transportId") {
					sTransportIdFromContent = mMetadata.value;
					return true;
				}
			});
			try {
				sPackageFromContent = JSON.parse(oContentData.data).packageName;
			} catch (e) {
				//when content is not in JSON format (Ex: js or code_ext file), package is undefined but does not break the code.
			}

			if ((sLayer === "USER") ||
				(sLayer === "LOAD") ||
				(sLayer === "VENDOR_LOAD") ||
				(!sTransportIdFromContent && (!sPackageFromContent || sPackageFromContent === "$TMP"))){
				sTransportId = undefined;
				this._saveFile(sLayer, oContentData.namespace, oContentData.fileName, oContentData.fileType, oContentData.data, sTransportId, sPackageName);
			} else if (sTransportIdFromContent === "ATO_NOTIFICATION") {
				sTransportId = sTransportIdFromContent;
				this._saveFile(sLayer, oContentData.namespace, oContentData.fileName, oContentData.fileType, oContentData.data, sTransportId, sPackageName);
			} else {
				var isPackageVisible = (sLayer === "VENDOR" || sLayer === "CUSTOMER_BASE") ? true : false;
				var oPackageInput = new Input({visible: isPackageVisible, placeholder: "Package name (Only necessary for cross client content)" });
				var oTransportInput = new Input({placeholder: "Transport ID or ATO_NOTIFICATION" });
				var oDialog = new Dialog({
					title: "{i18n>transportInput}",
					type: "Message",
					content: [
						new Text({text: "{i18n>transportInputDescription}"}),
						oPackageInput,
						oTransportInput],
					beginButton: new Button({
						text: "{i18n>confirm}",
						type: ButtonType.Reject,
						press: function () {
							sPackageName = oPackageInput.getValue();
							sTransportId = oTransportInput.getValue();
							oDialog.close();
							that._saveFile(sLayer, oContentData.namespace, oContentData.fileName, oContentData.fileType, oContentData.data, sTransportId, sPackageName);
						}
					}),
					endButton: new Button({
						text: "{i18n>cancel}",
						press: function () {
							oDialog.close();
						}
					}),
					afterClose: function () {
						oDialog.destroy();
					}
				});
				this.getView().addDependent(oDialog);
				oDialog.open();
			}
		}