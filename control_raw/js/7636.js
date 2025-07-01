function createSymbolSummaryForLib(lib) {
		let file = path.join(unpackedTestresourcesRoot, lib.replace(/\./g, "/"), "designtime/api.json");

		return readJSONFile(file).then(function (apijson) {
			if (!apijson.hasOwnProperty("symbols") || !Array.isArray(apijson.symbols)) {
				// Ignore libraries with invalid api.json content like empty object or non-array "symbols" property.
				return [];
			}
			return apijson.symbols.map(symbol => {
				let oReturn = {
					name: symbol.name,
					kind: symbol.kind,
					visibility: symbol.visibility,
					extends: symbol.extends,
					implements: symbol.implements,
					lib: lib
				};
				// We add deprecated member only when the control is deprecated to keep file size at check
				if (symbol.deprecated) {
					oReturn.deprecated = true;
				}
				collectLists(symbol);
				return oReturn;
			});
		})
	}