function (sBaseMetaPath, sChildMetaPath, mChildQueryOptions,
				fnFetchMetadata) {
			var sExpandSelectPath = "",
				i,
				aMetaPathSegments = sChildMetaPath.split("/"),
				oProperty,
				sPropertyMetaPath = sBaseMetaPath,
				mQueryOptions = {},
				mQueryOptionsForPathPrefix = mQueryOptions;

			if (sChildMetaPath === "") {
				return mChildQueryOptions;
			}

			for (i = 0; i < aMetaPathSegments.length; i += 1) {
				sPropertyMetaPath = _Helper.buildPath(sPropertyMetaPath, aMetaPathSegments[i]);
				sExpandSelectPath = _Helper.buildPath(sExpandSelectPath, aMetaPathSegments[i]);
				oProperty = fnFetchMetadata(sPropertyMetaPath).getResult();
				if (oProperty.$kind === "NavigationProperty") {
					mQueryOptionsForPathPrefix.$expand = {};
					mQueryOptionsForPathPrefix
						= mQueryOptionsForPathPrefix.$expand[sExpandSelectPath]
						= (i === aMetaPathSegments.length - 1) // last segment in path
							? mChildQueryOptions
							: {};
					_Helper.selectKeyProperties(mQueryOptionsForPathPrefix,
						fnFetchMetadata(sPropertyMetaPath + "/").getResult());
					sExpandSelectPath = "";
				} else if (oProperty.$kind !== "Property") {
					return undefined;
				}
			}
			if (oProperty.$kind === "Property") {
				if (Object.keys(mChildQueryOptions).length > 0) {
					Log.error("Failed to enhance query options for auto-$expand/$select as the"
							+ " child binding has query options, but its path '" + sChildMetaPath
							+ "' points to a structural property",
						JSON.stringify(mChildQueryOptions), sClassName);
					return undefined;
				}
				_Helper.addToSelect(mQueryOptionsForPathPrefix, [sExpandSelectPath]);
			}
			if ("$apply" in mChildQueryOptions) {
				Log.debug("Cannot wrap $apply into $expand: " + sChildMetaPath,
					JSON.stringify(mChildQueryOptions), sClassName);
				return undefined;
			}
			return mQueryOptions;
		}