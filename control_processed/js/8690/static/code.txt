function (sOverlayId) {
			var oOverlayDimensions = jQuery("#" + sOverlayId).rect();
			oOverlayDimensions.right = oOverlayDimensions.left + oOverlayDimensions.width;
			oOverlayDimensions.bottom = oOverlayDimensions.top + oOverlayDimensions.height;

			return oOverlayDimensions;
		}