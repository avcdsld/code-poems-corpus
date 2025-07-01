function (aOldColumns, aNewColumns, fnFormatterChanged) {
				var oNewColumn,
					oOldColumn,
					iResult = 0,
					i,
					n;

				if (!aOldColumns || aOldColumns.length !== aNewColumns.length) {
					return 2;
				}
				if (aOldColumns !== aNewColumns) {
					for (i = 0, n = aOldColumns.length; i < n; i += 1) {
						oOldColumn = aOldColumns[i];
						oNewColumn = aNewColumns[i];
						if (oOldColumn.grouped !== oNewColumn.grouped
							|| oOldColumn.inResult !== oNewColumn.inResult
							|| oOldColumn.level !== oNewColumn.level
							|| oOldColumn.name !== oNewColumn.name
							|| oOldColumn.total !== oNewColumn.total
							|| oOldColumn.visible !== oNewColumn.visible) {
							return 2;
						}
						if (oOldColumn.formatter !== oNewColumn.formatter) {
							iResult = 1;
							if (fnFormatterChanged) {
								fnFormatterChanged(oNewColumn);
							}
						}
					}
				}

				return iResult;
			}