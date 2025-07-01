function(oList, bArrow){
		function getPrevOnSameLevel(oLst){
			var oParentRef = oLst.getParent();
			var aParentSubLists = oParentRef.getSubLists();
			var idx = oParentRef.indexOfSubList(oLst) - 1;
			if (idx >= 0) {
				return aParentSubLists[idx];
			}
			return null;
		}

		function getListOrLastChild(oLst){
			var aSubLists = oLst.getSubLists();
			if (aSubLists.length > 0) {
				return getListOrLastChild(aSubLists[aSubLists.length - 1]);
			}
			return oLst;
		}

		if (oList._iLevel == 0) {
			return null;
		} else if (oList._iLevel == 1) {
			if (bArrow) {
				return null;
			}
			var oPrevList = getPrevOnSameLevel(oList);
			if (oPrevList) {
				return oPrevList;
			}
			return oList.getParent();
		} else if (oList._iLevel > 1) {
			var oPrevList = getPrevOnSameLevel(oList);
			if (oPrevList) {
				return getListOrLastChild(oPrevList);
			}
			var oParent = oList.getParent();
			if (oParent._iLevel >= 1) {
				return oParent;
			}
		}
		return null;
	}