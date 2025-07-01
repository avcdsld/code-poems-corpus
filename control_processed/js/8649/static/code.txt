function(oPosition) {
		var oPos = oPosition.getComputedPosition();

		var addStyle = function(oPosition, aBuffer, sPos, sVal){
			if (sVal) {
				aBuffer.push(sPos + ":" + sVal + ";");
			}
		};

		var aBuffer = [];
		addStyle(oPosition, aBuffer, "top", oPos.top);
		addStyle(oPosition, aBuffer, "bottom", oPos.bottom);
		addStyle(oPosition, aBuffer, "left", oPos.left);
		addStyle(oPosition, aBuffer, "right", oPos.right);
		addStyle(oPosition, aBuffer, "width", oPos.width);
		addStyle(oPosition, aBuffer, "height", oPos.height);

		return aBuffer.join("");
	}