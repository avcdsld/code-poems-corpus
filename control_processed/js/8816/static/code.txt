function(oCellRef) {
			var oCellInfo;
			var $Cell = jQuery(oCellRef);
			var sColumnId;
			var oColumn;
			var rRowIndex;
			var aRowIndexMatch;
			var iRowIndex;

			// Initialize cell info object with default values.
			oCellInfo = {
				type: 0,
				cell: null,
				rowIndex: null,
				columnIndex: null,
				columnSpan: null
			};

			if ($Cell.hasClass("sapUiTableDataCell")) {
				sColumnId = $Cell.attr("data-sap-ui-colid");
				oColumn = sap.ui.getCore().byId(sColumnId);

				oCellInfo.type = TableUtils.CELLTYPE.DATACELL;
				oCellInfo.rowIndex = parseInt($Cell.parent().attr("data-sap-ui-rowindex"));
				oCellInfo.columnIndex = oColumn.getIndex();
				oCellInfo.columnSpan = 1;

			} else if ($Cell.hasClass("sapUiTableHeaderDataCell")) {
				rRowIndex = /_([\d]+)/;
				sColumnId = $Cell.attr("id");
				aRowIndexMatch = rRowIndex.exec(sColumnId);
				iRowIndex = aRowIndexMatch && aRowIndexMatch[1] != null ? parseInt(aRowIndexMatch[1]) : 0;

				oCellInfo.type = TableUtils.CELLTYPE.COLUMNHEADER;
				oCellInfo.rowIndex = iRowIndex;
				oCellInfo.columnIndex = parseInt($Cell.attr("data-sap-ui-colindex"));
				oCellInfo.columnSpan = parseInt($Cell.attr("colspan") || 1);

			} else if ($Cell.hasClass("sapUiTableRowSelectionCell")) {
				oCellInfo.type = TableUtils.CELLTYPE.ROWHEADER;
				oCellInfo.rowIndex = parseInt($Cell.attr("data-sap-ui-rowindex"));
				oCellInfo.columnIndex = -1;
				oCellInfo.columnSpan = 1;

			} else if ($Cell.hasClass("sapUiTableRowActionCell")) {
				oCellInfo.type = TableUtils.CELLTYPE.ROWACTION;
				oCellInfo.rowIndex = parseInt($Cell.attr("data-sap-ui-rowindex"));
				oCellInfo.columnIndex = -2;
				oCellInfo.columnSpan = 1;

			} else if ($Cell.hasClass("sapUiTableRowSelectionHeaderCell")) {
				oCellInfo.type = TableUtils.CELLTYPE.COLUMNROWHEADER;
				oCellInfo.columnIndex = -1;
				oCellInfo.columnSpan = 1;

			} else if ($Cell.hasClass("sapUiTablePseudoCell")) {
				sColumnId = $Cell.attr("data-sap-ui-colid");
				oColumn = sap.ui.getCore().byId(sColumnId);

				oCellInfo.type = TableUtils.CELLTYPE.PSEUDO;
				oCellInfo.rowIndex = -1;
				oCellInfo.columnIndex = oColumn ? oColumn.getIndex() : -1;
				oCellInfo.columnSpan = 1;
			}

			// Set the cell object for easier access to the cell for the caller.
			if (oCellInfo.type !== 0) {
				oCellInfo.cell = $Cell;
			}

			/**
			 * Function to check whether a cell is of certain types. Cell types are flags and have to be passed as a bitmask.
			 * Returns true if the cell is of one of the specified types, otherwise false. Also returns false if no or an invalid bitmask
			 * is specified.
			 *
			 * @alias sap.ui.table.TableUtils.CellInfo#isOfType
			 * @param {int} cellTypeMask Bitmask of cell types to check.
			 * @returns {boolean} Whether the specified cell type mask matches the type of the cell.
			 * @see CELLTYPE
			 */
			oCellInfo.isOfType = function(cellTypeMask) {
				if (cellTypeMask == null) {
					return false;
				}
				return (this.type & cellTypeMask) > 0;
			};

			return oCellInfo;
		}