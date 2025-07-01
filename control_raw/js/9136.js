function removeTabbable(oBlockSpan, fnRedirectFocus) {
			if (oBlockSpan.parentNode) {
				oBlockSpan.parentNode.removeChild(oBlockSpan);
			}
			oBlockSpan.removeEventListener('focusin', fnRedirectFocus);
		}