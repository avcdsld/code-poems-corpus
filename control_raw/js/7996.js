function(bAsKeyUser) {
			var oDescriptor = fnGetDescriptor();

			return new Promise(function(resolve) {
				var fnCancel = function() {
					AppVariantUtils.closeOverviewDialog();
				};
				sap.ui.require(["sap/ui/rta/appVariant/AppVariantOverviewDialog"], function(AppVariantOverviewDialog) {
					if (!oAppVariantOverviewDialog) {
						oAppVariantOverviewDialog = new AppVariantOverviewDialog({
							idRunningApp: oDescriptor["sap.app"].id,
							isOverviewForKeyUser: bAsKeyUser
						});
					}

					oAppVariantOverviewDialog.attachCancel(fnCancel);

					oAppVariantOverviewDialog.oPopup.attachOpened(function() {
						resolve(oAppVariantOverviewDialog);
					});

					oAppVariantOverviewDialog.open();
				});
			});
		}