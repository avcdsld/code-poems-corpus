function(oTable, oElement, bIncludePseudoCells) {
			bIncludePseudoCells = bIncludePseudoCells === true;

			var $Element = jQuery(oElement);
			var $Cell = TableUtils.getCell(oTable, oElement, bIncludePseudoCells);

			if (!$Cell || $Cell[0] === $Element[0]) {
				return null; // The element is not inside a table cell.
			} else {
				return $Cell;
			}
		}