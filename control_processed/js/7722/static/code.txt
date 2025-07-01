function _createRFLayoutData(iWeight, bLinebreak, bLinebreakable, iMinWidth) {

		var oLayout = new ResponsiveFlowLayoutData({weight:iWeight,linebreak:bLinebreak === true,linebreakable: bLinebreakable === true});
		if (iMinWidth) {
			oLayout.setMinWidth(iMinWidth);
		}
		this._aLayouts.push(oLayout.getId());
		return oLayout;

	}