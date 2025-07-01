function _getFieldLayoutData(oField){

		var oLayoutData;

		switch (this.getLayout()) {
		case SimpleFormLayout.ResponsiveLayout:
			oLayoutData = FormLayout.prototype.getLayoutDataForElement(oField, "sap.ui.layout.ResponsiveFlowLayoutData");
			break;
		case SimpleFormLayout.GridLayout:
			oLayoutData = FormLayout.prototype.getLayoutDataForElement(oField, "sap.ui.layout.form.GridElementData");
			break;
		case SimpleFormLayout.ResponsiveGridLayout:
			oLayoutData = FormLayout.prototype.getLayoutDataForElement(oField, "sap.ui.layout.GridData");
			break;
		case SimpleFormLayout.ColumnLayout:
			oLayoutData = FormLayout.prototype.getLayoutDataForElement(oField, "sap.ui.layout.form.ColumnElementData");
			break;
			// no default
		}

		return oLayoutData;

	}