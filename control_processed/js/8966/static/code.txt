function getType(oNode) {
			var oPropertyMetadata;

			if (oNode.type) {
				return {
					$Type : oNode.type
				};
			}
			if (oNode.id === "PATH") {
				oPropertyMetadata = that.oModelInterface
					.fetchMetadata(sMetaPath + "/" + oNode.value).getResult();
				if (!oPropertyMetadata) {
					throw new Error("Invalid filter path: " + oNode.value);
				}
				return {
					path : oNode.value,
					$Type : oPropertyMetadata.$Type,
					$v2Type : oPropertyMetadata.$v2Type
				};
			}
			// oNode must have id "FUNCTION" and type undefined here. So it must be either ceiling,
			// floor or round and the return type is determined from the first and only parameter.
			return getType(oNode.parameters[0]);
		}