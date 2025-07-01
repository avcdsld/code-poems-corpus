function(oEvent) {
			var oTable = this.getTable();
			if (!oTable || TableUtils.getCellInfo(oEvent.target).cell == null) {
				return;
			}
			if (oTable._mTimeouts._cleanupACCExtension) {
				clearTimeout(oTable._mTimeouts._cleanupACCExtension);
				oTable._mTimeouts._cleanupACCExtension = null;
			}
			this.updateAccForCurrentCell("Focus");
		}