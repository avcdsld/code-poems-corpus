function setMode(oBinding, iIndex) {
				if (oBinding.parts) {
					oBinding.parts.forEach(function (vPart, i) {
						if (typeof vPart === "string") {
							vPart = oBinding.parts[i] = {path : vPart};
						}
						setMode(vPart, i);
					});
					b2ndLevelMergedNeeded = b2ndLevelMergedNeeded || iIndex !== undefined;
				} else {
					oBinding.mode = oBindingMode;
				}
			}