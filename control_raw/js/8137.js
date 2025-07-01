function decompressIndex(oIndex) {

		function decompressField(sFieldName) {

			var tfValues = oIndex.lunr.index[sFieldName].tfValues;
			tfValues[0] = NaN; // restore NaN, JSON converts it to null
			oIndex.lunr.index[sFieldName].tfValues = undefined;

			function decompressArrayItemsByLength(sCompressed) {
				var aDocIds = [];
				sCompressed.split(",").forEach(function(sCompressedOfLength) {
					var aParts = sCompressedOfLength.split(":"),
						iKey = parseInt(aParts[0]),
						sDocIdsOfLen = aParts[1];

					while (sDocIdsOfLen.length > 0) {
						aDocIds.push(sDocIdsOfLen.slice(0, iKey));
						sDocIdsOfLen = sDocIdsOfLen.slice(iKey);
					}
				});
				return aDocIds;
			}

			function decompressDocs(oNode) {
				var oDocs = oNode.docs,
					iCount = 0;
				if ( oDocs === undefined ) {
					oNode.docs = {};
				} else {
					Object.keys(oDocs).forEach(function (sDocKey) {
						if ( typeof oDocs[sDocKey] === 'number' ) {
							oDocs[sDocKey] = {
								tf: tfValues[ oDocs[sDocKey] ]
							};
						}
						if ( sDocKey.indexOf(':') >= 0 ) {
							var aDocIds = decompressArrayItemsByLength(sDocKey);
							aDocIds.forEach( function (docKeyPart) {
								oDocs[docKeyPart] = oDocs[sDocKey];
								iCount++;
							});
							oDocs[sDocKey] = undefined;
						} else {
							iCount++;
						}
					});
				}
				if ( oNode.df === undefined ) {
					oNode.df = iCount;
				}
			}

			function decompressIndexNode(oNode) {
				decompressDocs(oNode);
				Object.keys(oNode).forEach( function (sKey) {
					if ( sKey !== 'docs' && sKey !== 'df' ) {
						var oValue = oNode[sKey];
						var iLength = sKey.length;
						if ( iLength > 1 ) {
							while ( --iLength > 0 ) {
								var oTmp = {};
								oTmp[ sKey.charAt(iLength) ] = oValue;
								oValue = oTmp;
							}
							oNode[ sKey.charAt(0) ] = oValue;
							oNode[sKey] = undefined;
						}
						decompressIndexNode(oValue);
					}
				} );
			}

			decompressIndexNode(oIndex.lunr.index[sFieldName].root);
		}

		function traverse(oNode,fnProcessNode) {
			for (var i in oNode) {
				fnProcessNode.apply(oNode,[i,oNode[i]]);
				if (oNode[i] !== null && typeof (oNode[i]) == "object") {
					//going one step down in the object tree!!
					traverse(oNode[i],fnProcessNode);
				}
			}
		}

		function deleteUndefinedEntries(sKey, oValue) {
			if (oValue === undefined) {
				delete this[sKey];
			}
		}

		INDEXED_FIELDS.forEach(function(sFieldName) {
			decompressField(sFieldName);
		});

		// return a deep copy to get rid of properties with value "undefined"
		traverse(oIndex, deleteUndefinedEntries);

		return oIndex;
	}