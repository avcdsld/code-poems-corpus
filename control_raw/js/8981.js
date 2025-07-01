function fetchType(sMetaPath) {
			aPromises.push(that.oRequestor.fetchTypeForPath(sMetaPath).then(function (oType) {
				var oMessageAnnotation = that.oRequestor.getModelInterface()
						.fetchMetadata(sMetaPath + "/" + sMessagesAnnotation).getResult();

				if (oMessageAnnotation) {
					oType = Object.create(oType);
					oType[sMessagesAnnotation] = oMessageAnnotation;
				}

				mTypeForMetaPath[sMetaPath] = oType;
				if (oType && oType.$Key) {
					oType.$Key.forEach(function (vKey) {
						var iIndexOfSlash, sKeyPath;

						if (typeof vKey !== "string") {
							sKeyPath = vKey[Object.keys(vKey)[0]];
							iIndexOfSlash = sKeyPath.lastIndexOf("/");
							if (iIndexOfSlash >= 0) {
								// drop the property name and fetch the type containing it
								fetchType(sMetaPath + "/" + sKeyPath.slice(0, iIndexOfSlash));
							}
						}
					});
				}
			}));
		}