function(oTable) {
			if (!oTable || !oTable._oCellContextMenu) {
				return;
			}

			oTable._oCellContextMenu.destroy();
			oTable._oCellContextMenu = null;
		}