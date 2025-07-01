function getErrorMessage(oType) {
		return sap.ui.getCore().getLibraryResourceBundle().getText("EnterTime",
			[oType.formatValue(oDemoTime, "string")]);
	}