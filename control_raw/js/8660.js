function(oEvent) {
			var oTouch;

			if (bHandleEvent) {
				oTouch = oEvent.touches[0];

				// Check if the finger is moved. When the finger was moved, no "click" event is fired.
				if (Math.abs(oTouch.clientX - iStartX) > 10 || Math.abs(oTouch.clientY - iStartY) > 10) {
					bIsMoved = true;
				}

				if (bIsMoved) {

					// Fire "mousemove" event only when the finger was moved. This is to prevent unwanted movements.
					fireMouseEvent("mousemove", oEvent);
				}
			}
		}