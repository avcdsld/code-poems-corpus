function (oContPos, oPopover, oViewport) {
			this.getPopover().setShowArrow(false);
			var oPos = {};

			if (oViewport.height - 10 - oContPos.y >= oPopover.height) {
				oPos.top = oContPos.y;
				this.getPopover().setPlacement("Bottom");
			} else if (oContPos.y >= oPopover.height) {
				oPos.top = oContPos.y;
				this.getPopover().setPlacement("Top");
			} else {
				oPos.top = oViewport.height - oPopover.height;
				this.getPopover().setPlacement("Bottom");
			}

			if (oViewport.width - oContPos.x >= oPopover.width) {
				oPos.left = oContPos.x;
			} else if (oContPos.x >= oPopover.width) {
				oPos.left = oContPos.x - oPopover.width / 2;
			} else {
				oPos.left = oViewport.width - oPopover.width;
			}

			return oPos;
		}