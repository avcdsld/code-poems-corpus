function visitInstance(oInstance, sMetaPath, sInstancePath, sContextUrl, iIndex) {
			var aMatches,
				sPredicate,
				oType = mTypeForMetaPath[sMetaPath],
				sMessageProperty = oType && oType[sMessagesAnnotation]
					&& oType[sMessagesAnnotation].$Path,
				aMessages;

			sContextUrl = buildContextUrl(sContextUrl, oInstance["@odata.context"]);
			sPredicate = that.calculateKeyPredicate(oInstance, mTypeForMetaPath, sMetaPath);
			if (iIndex !== undefined) {
				sInstancePath = _Helper.buildPath(sInstancePath, sPredicate || iIndex);
			} else if (!bKeepTransientPath && sPredicate) {
				aMatches = rEndsWithTransientPredicate.exec(sInstancePath);
				if (aMatches) {
					sInstancePath = sInstancePath.slice(0, -aMatches[0].length) + sPredicate;
				}
			}
			if (sRootPath && !aCachePaths) {
				// remove messages only for the part of the cache that is updated
				aCachePaths = [sInstancePath];
			}
			if (sMessageProperty) {
				aMessages = _Helper.drillDown(oInstance, sMessageProperty.split("/"));
				if (aMessages !== undefined) {
					addMessages(aMessages, sInstancePath, sContextUrl);
				}
			}

			Object.keys(oInstance).forEach(function (sProperty) {
				var sCount,
					sPropertyMetaPath = sMetaPath + "/" + sProperty,
					vPropertyValue = oInstance[sProperty],
					sPropertyPath = _Helper.buildPath(sInstancePath, sProperty);

				if (sProperty.endsWith("@odata.mediaReadLink")) {
					oInstance[sProperty] = _Helper.makeAbsolute(vPropertyValue, sContextUrl);
				}
				if (sProperty.includes("@")) { // ignore other annotations
					return;
				}
				if (Array.isArray(vPropertyValue)) {
					vPropertyValue.$created = 0; // number of (client-side) created elements
					// compute count
					vPropertyValue.$count = undefined; // see setCount
					sCount = oInstance[sProperty + "@odata.count"];
					// Note: ignore change listeners, because any change listener that is already
					// registered, is still waiting for its value and gets it via fetchValue
					if (sCount) {
						setCount({}, "", vPropertyValue, sCount);
					} else if (!oInstance[sProperty + "@odata.nextLink"]) {
						// Note: This relies on the fact that $skip/$top is not used on nested lists
						setCount({}, "", vPropertyValue, vPropertyValue.length);
					}
					visitArray(vPropertyValue, sPropertyMetaPath, sPropertyPath,
						buildContextUrl(sContextUrl, oInstance[sProperty + "@odata.context"]));
				} else if (vPropertyValue && typeof vPropertyValue === "object") {
					visitInstance(vPropertyValue, sPropertyMetaPath, sPropertyPath, sContextUrl);
				}
			});
		}