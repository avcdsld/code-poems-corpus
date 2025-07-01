function(oRoadMap, bLast){
		var iScrollWidth = oRoadMap.$("steparea").get(0).scrollWidth;
		if (sap.ui.getCore().getConfiguration().getRTL() && Device.browser.webkit) {
			return bLast ? 0 : ( -1) * iScrollWidth;
		}
		return bLast ? iScrollWidth : 0;
	}