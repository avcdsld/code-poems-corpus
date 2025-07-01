function(oTable, nScrollPosition, sTrigger, bPreventScroll) {
			sTrigger = sTrigger == null ? ScrollTrigger.EXTENSION : sTrigger;

			var oScrollExtension = oTable ? oTable._getScrollExtension() : null;
			var oVSb = oScrollExtension ? oScrollExtension.getVerticalScrollbar() : null;

			if (!oTable || !oVSb || !oScrollExtension.isVerticalScrollbarRequired() || internal(oTable).bVerticalScrollingSuspended) {
				log("VerticalScrollingHelper#updateScrollPosition: Not executed - Guard clause not passed", oTable);
				return;
			}

			var nOldScrollPosition = internal(oTable).nVerticalScrollPosition;
			var iMaxScrollPosition = VerticalScrollingHelper.getScrollRange(oTable);

			if (nScrollPosition == null) {
				var iFirstVisibleRowIndex = oTable.getFirstVisibleRow();
				var iMaxFirstRenderedRowIndex = oTable._getMaxFirstRenderedRowIndex();

				if (iFirstVisibleRowIndex > iMaxFirstRenderedRowIndex) {
					// The first visible row is inside the buffer. The table will be scrolled to the maximum possible first rendered row to receive the
					// heights of the rows in the buffer. The first visible row will then be correctly displayed on top when the inner scroll position
					// is updated. oScrollExtension process is not required for the first row in the buffer.
					nScrollPosition = iMaxScrollPosition;
					internal(oTable).iFirstVisibleRowInBuffer = iFirstVisibleRowIndex - iMaxFirstRenderedRowIndex;
				} else {
					nScrollPosition = iFirstVisibleRowIndex * VerticalScrollingHelper.getScrollRangeRowFraction(oTable);
					internal(oTable).iFirstVisibleRowInBuffer = null;
				}
			} else {
				internal(oTable).iFirstVisibleRowInBuffer = null;
			}
			internal(oTable).nVerticalScrollPosition = Math.min(Math.max(0, nScrollPosition), iMaxScrollPosition);

			log("VerticalScrollingHelper#updateScrollPosition: From " + nOldScrollPosition + " to " + internal(oTable).nVerticalScrollPosition
				+ " (diff: " + (internal(oTable).nVerticalScrollPosition - nOldScrollPosition) + ", trigger: " + sTrigger + ")", oTable);

			if (bPreventScroll === true) {
				log("VerticalScrollingHelper#updateScrollPosition: Scrolling prevented", oTable);
				return;
			}

			window.cancelAnimationFrame(oTable._mAnimationFrames.verticalScrollUpdate);
			delete oTable._mAnimationFrames.verticalScrollUpdate;

			switch (sTrigger) {
				case ScrollTrigger.SCROLLBAR:
					clearTimeout(oTable._mTimeouts.largeDataScrolling);
					delete oTable._mTimeouts.largeDataScrolling;

					if (oTable._bLargeDataScrolling && !internal(oTable).bIsScrolledVerticallyByWheel) {
						oTable._mTimeouts.largeDataScrolling = setTimeout(function() {
							delete oTable._mTimeouts.largeDataScrolling;
							VerticalScrollingHelper.updateFirstVisibleRow(oTable);
						}, 300);
					} else {
						VerticalScrollingHelper.updateFirstVisibleRow(oTable);
					}
					break;
				case ScrollTrigger.KEYBOARD:
				case ScrollTrigger.MOUSEWHEEL:
				case ScrollTrigger.TOUCH:
				case ScrollTrigger.EXTENSION:
				case ScrollTrigger.TABLE:
					var iNewScrollTop = 0;
					var iVerticalScrollRange = VerticalScrollingHelper.getScrollRange(oTable);

					// As soon as the scroll position is > 0, scrollTop must be set to 1. Otherwise the user cannot scroll back to the first row with the
					// scrollbar. The same applies vice versa if the scroll position is at the bottom.
					if (internal(oTable).nVerticalScrollPosition > 0 && internal(oTable).nVerticalScrollPosition < 0.5) {
						iNewScrollTop = 1;
					} else if (internal(oTable).nVerticalScrollPosition >= iVerticalScrollRange - 0.5
							   && internal(oTable).nVerticalScrollPosition < iVerticalScrollRange) {
						iNewScrollTop = iVerticalScrollRange - 1;
					} else {
						iNewScrollTop = Math.round(internal(oTable).nVerticalScrollPosition);
					}

					if (oVSb.scrollTop !== iNewScrollTop) {
						log("VerticalScrollingHelper#updateScrollPosition: scrollTop will be set asynchronously", oTable);

						oTable._mAnimationFrames.verticalScrollUpdate = window.requestAnimationFrame(function() {
							var nOldScrollTop = oVSb.scrollTop;

							delete oTable._mAnimationFrames.verticalScrollUpdate;

							log("VerticalScrollingHelper#updateScrollPosition: (async) Set scrollTop from " + nOldScrollTop + " to " + iNewScrollTop,
								oTable);

							oVSb.scrollTop = iNewScrollTop;
							oVSb._scrollTop = oVSb.scrollTop;

							if (iNewScrollTop === iVerticalScrollRange && iNewScrollTop !== oVSb.scrollTop) {
								log("VerticalScrollingHelper#updateScrollPosition: (async) Adjusted from "
									+ internal(oTable).nVerticalScrollPosition + " to " + oVSb.scrollTop, oTable);
								internal(oTable).nVerticalScrollPosition = oVSb.scrollTop;
							}

							VerticalScrollingHelper.updateFirstVisibleRow(oTable);
						});
					} else if (internal(oTable).nVerticalScrollPosition !== nOldScrollPosition) {
						log("VerticalScrollingHelper#updateScrollPosition: firstVisibleRow will be set asynchronously", oTable);

						oTable._mAnimationFrames.verticalScrollUpdate = window.requestAnimationFrame(function() {
							delete oTable._mAnimationFrames.verticalScrollUpdate;
							VerticalScrollingHelper.updateFirstVisibleRow(oTable);
						});
					} else {
						log("VerticalScrollingHelper#updateScrollPosition: scrollTop and nVerticalScrollPosition not changed"
							+ " -> update inner vertical scroll position", oTable);

						// Even if the scroll position did not change, the inner scroll position might need to be updated. For example, because it
						// could have been reset to 0 by a re-rendering.
						oScrollExtension.updateInnerVerticalScrollPosition();
					}
					break;
				default:
			}
		}