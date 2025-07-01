function(oTable, vRowIndicator, bSelect, fnDoSelect) {
			if (!oTable ||
				!oTable.getBinding("rows") ||
				oTable.getSelectionMode() === SelectionMode.None ||
				vRowIndicator == null) {

				return false;
			}

			function setSelectionState(iAbsoluteRowIndex) {
				if (!oTable._isRowSelectable(iAbsoluteRowIndex)) {
					return false;
				}

				oTable._iSourceRowIndex = iAbsoluteRowIndex; // To indicate that the selection was changed by user interaction.

				var bSelectionChanged = false;

				if (fnDoSelect) {
					bSelectionChanged = fnDoSelect(iAbsoluteRowIndex, bSelect);
				} else if (oTable.isIndexSelected(iAbsoluteRowIndex)) {
					if (bSelect !== true) {
						bSelectionChanged = true;
						oTable.removeSelectionInterval(iAbsoluteRowIndex, iAbsoluteRowIndex);
					}
				} else if (bSelect !== false) {
					bSelectionChanged = true;
					oTable.addSelectionInterval(iAbsoluteRowIndex, iAbsoluteRowIndex);
				}

				delete oTable._iSourceRowIndex;
				return bSelectionChanged;
			}

			// Variable vRowIndicator is a row index value.
			if (typeof vRowIndicator === "number") {
				if (vRowIndicator < 0 || vRowIndicator >= oTable._getTotalRowCount()) {
					return false;
				}
				return setSelectionState(vRowIndicator);

				// Variable vRowIndicator is a jQuery object or DOM element.
			} else {
				var $Cell = jQuery(vRowIndicator);
				var oCellInfo = TableUtils.getCellInfo($Cell[0]);
				var bIsRowSelectionAllowed = TableUtils.isRowSelectionAllowed(oTable);

				if (!TableUtils.Grouping.isInGroupingRow($Cell[0])
					&& ((oCellInfo.isOfType(TableUtils.CELLTYPE.DATACELL | TableUtils.CELLTYPE.ROWACTION) && bIsRowSelectionAllowed)
						|| (oCellInfo.isOfType(TableUtils.CELLTYPE.ROWHEADER) && TableUtils.isRowSelectorSelectionAllowed(oTable)))) {

					var iAbsoluteRowIndex;
					if (oCellInfo.isOfType(TableUtils.CELLTYPE.DATACELL)) {
						iAbsoluteRowIndex = oTable
							.getRows()[parseInt($Cell.closest("tr", oTable.getDomRef()).attr("data-sap-ui-rowindex"))]
							.getIndex();
					} else { // CELLTYPES.ROWHEADER, CELLTYPES.ROWACTION
						iAbsoluteRowIndex = oTable.getRows()[parseInt($Cell.attr("data-sap-ui-rowindex"))].getIndex();
					}

					return setSelectionState(iAbsoluteRowIndex);
				}

				return false;
			}
		}