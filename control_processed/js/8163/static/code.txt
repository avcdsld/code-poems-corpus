function(oTable) {
			var oScrollExtension = oTable._getScrollExtension();
			var oHSb = oScrollExtension.getHorizontalScrollbar();
			var aScrollAreas = HorizontalScrollingHelper.getScrollAreas(oTable);

			if (oScrollExtension._onHorizontalScrollEventHandler) {
				for (var i = 0; i < aScrollAreas.length; i++) {
					aScrollAreas[i].removeEventListener("scroll", oScrollExtension._onHorizontalScrollEventHandler);
					delete aScrollAreas[i]._scrollLeft;
				}
				delete oScrollExtension._onHorizontalScrollEventHandler;
			}

			if (oHSb && oScrollExtension._onHorizontalScrollbarMouseDownEventHandler) {
				oHSb.removeEventListener("mousedown", oScrollExtension._onHorizontalScrollbarMouseDownEventHandler);
				delete oScrollExtension._onHorizontalScrollbarMouseDownEventHandler;
			}
		}