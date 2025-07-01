function addSelects(vSelects, sExpandPath) {
			if (!Array.isArray(vSelects)) {
				vSelects = vSelects.split(",");
			}
			vSelects.forEach(function (sSelect) {
				var iIndex = sSelect.indexOf("/");

				if (iIndex >= 0 && sSelect.indexOf(".") < 0) {
					// only strip if there is no type cast and no bound action (avoid "correcting"
					// unsupported selects in V2)
					sSelect = sSelect.slice(0, iIndex);
				}
				mSelects[_Helper.buildPath(sExpandPath, sSelect)] = true;
			});
		}