function triggerBeforeRendering(oControl){
			bLocked = true;
			try {
				var oEvent = jQuery.Event("BeforeRendering");
				// store the element on the event (aligned with jQuery syntax)
				oEvent.srcControl = oControl;
				oControl._handleEvent(oEvent);
			} finally {
				bLocked = false;
			}
		}