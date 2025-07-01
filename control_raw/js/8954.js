function getInfo() {
				var collection = mRegistry[collectionName];
				var info = collection && collection[iconName];

				// convert raw data lazily to the icon info
				if (typeof info === 'number') {
					mRegistry[collectionName][iconName] = undefined; // avoid duplicate icon warning
					info = IconPool.addIcon(iconName, collectionName, {
						fontFamily: mFontRegistry[collectionName].config.fontFamily,
						content: info & 0xFFFF,
						suppressMirroring: !!(info & 0x10000),
						resourceBundle: getCoreResourceBundle()
					});
				}

				return info;
			}