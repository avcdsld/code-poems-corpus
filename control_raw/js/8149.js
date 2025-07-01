function(oTable) {
			if (TableGrouping.isGroupMode(oTable) || TableGrouping.isTreeMode(oTable)) {
				var oBinding = oTable.getBinding("rows");
				var oRowBindingInfo = oTable.getBindingInfo("rows");
				var aRows = oTable.getRows();
				var iCount = aRows.length;
				var iRow;

				if (oBinding) {
					for (iRow = 0; iRow < iCount; iRow++) {
						var oRowGroupInfo = TableGrouping.getRowGroupInfo(oTable, aRows[iRow], oBinding, oRowBindingInfo);
						TableGrouping.updateTableRowForGrouping(oTable, aRows[iRow], oRowGroupInfo.isHeader, oRowGroupInfo.expanded,
							oRowGroupInfo.hidden, false, oRowGroupInfo.level, oRowGroupInfo.title);
					}
				} else {
					for (iRow = 0; iRow < iCount; iRow++) {
						TableGrouping.cleanupTableRowForGrouping(oTable, aRows[iRow]);
					}
				}
			}
		}