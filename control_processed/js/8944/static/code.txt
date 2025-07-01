function (oTree) {
			var sDebugString = this.toDebugInfo(oTree);

			if (sDebugString === true) {
				return 1;
			} else if (sDebugString) {
				return sDebugString.split(",").length;
			}
			return 0;
		}