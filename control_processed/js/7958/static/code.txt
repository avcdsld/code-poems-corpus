function(oThis, oEvent, sDir){
		oEvent.stopPropagation();
		oEvent.preventDefault();

		if (!oThis.sCurrentFocusedItemRefId) {
			return;
		}

		var sFollowingFocusItemId = null;
		if (oThis.sLastVisibleItemId && ((oThis.sCurrentFocusedItemRefId == oThis.sLastVisibleItemId && sDir == "next") || sDir == "last")) {
			sFollowingFocusItemId = oThis.getId() + "-ovrflw";
		} else if (oThis.sLastVisibleItemId && oThis.sCurrentFocusedItemRefId == oThis.getId() + "-ovrflw" && sDir == "prev") {
			sFollowingFocusItemId = oThis.sLastVisibleItemId;
		} else {
			var sFoo = sDir + "All";
			var bIsJumpToEnd = false;
			if (sDir == "first") {
				sFoo = "prevAll";
				bIsJumpToEnd = true;
			} else if (sDir == "last") {
				sFoo = "nextAll";
				bIsJumpToEnd = true;
			}

			var jCurrentFocusItem = jQuery(document.getElementById(oThis.sCurrentFocusedItemRefId));
			var jFollowingItems = jCurrentFocusItem[sFoo](":visible");

			sFollowingFocusItemId = jQuery(jFollowingItems.get(bIsJumpToEnd ? jFollowingItems.length - 1 : 0)).attr("id");
		}
		if (sFollowingFocusItemId) {
			oThis.sCurrentFocusedItemRefId = sFollowingFocusItemId;
			document.getElementById(sFollowingFocusItemId).focus();
		}
	}