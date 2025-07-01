function(oRectOne, oRectTwo) {
		if ((!oRectOne && oRectTwo) || (oRectOne && !oRectTwo)) {
			return false;
		}

		if (!oRectOne && !oRectTwo) {
			return true;
		}

		var iPuffer = 3;
		var iLeft = Math.abs(oRectOne.left - oRectTwo.left);
		var iTop = Math.abs(oRectOne.top - oRectTwo.top);
		var iWidth = Math.abs(oRectOne.width - oRectTwo.width);
		var iHeight = Math.abs(oRectOne.height - oRectTwo.height);

		// check if the of has moved more pixels than set in the puffer
		// Puffer is needed if the opener changed its position only by 1 pixel:
		// this happens in IE if a control was clicked (is a reported IE bug)
		if (iLeft > iPuffer || iTop > iPuffer || iWidth > iPuffer || iHeight > iPuffer) {
			return false;
		}
		return true;
	}