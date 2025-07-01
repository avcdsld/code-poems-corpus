function(oThis, oEvent){
		oThis._sSearchQuery = oEvent.getParameter("query"); //Store the value until next Search
		oThis.fireSearch({query: oThis._sSearchQuery});
		oThis._bDetailsVisible = true;
		oThis.invalidate();
	}