function (aParts, fnRootFormatter) {
				var bMergeNeeded = false,
					vPropertySetting;

				aParts = aParts.slice(); // shallow copy to avoid changes visible to caller
				aParts.forEach(function (vPart, i) {
					switch (typeof vPart) {
					case "boolean":
					case "number":
					case "undefined":
						bMergeNeeded = true;
						break;

					case "string":
						vPropertySetting = BindingParser.complexParser(vPart, null, true, true);
						if (vPropertySetting !== undefined) {
							if (vPropertySetting.functionsNotFound) {
								throw new Error("Function name(s) "
									+ vPropertySetting.functionsNotFound.join(", ")
									+  " not found");
							}
							aParts[i] = vPart = vPropertySetting;
						}
						// falls through
					case "object":
						// merge is needed if some parts are constants or again have parts
						// Note: a binding info object has either "path" or "parts"
						if (!vPart || typeof vPart !== "object" || !("path" in vPart)) {
							bMergeNeeded = true;
						}
						break;

					default:
						throw new Error("Unsupported part: " + vPart);
					}
				});

				vPropertySetting = {
					formatter : fnRootFormatter,
					parts : aParts
				};
				if (bMergeNeeded) {
					BindingParser.mergeParts(vPropertySetting);
				}

				if (vPropertySetting.parts.length === 0) {
					// special case: all parts are constant values, call formatter once
					vPropertySetting = vPropertySetting.formatter && vPropertySetting.formatter();
					if (typeof vPropertySetting === "string") {
						vPropertySetting = BindingParser.complexParser.escape(vPropertySetting);
					}
				} else if (vPropertySetting.parts.length === 1) {
					// special case: a single property setting only
					// Note: sap.ui.base.ManagedObject#_bindProperty cannot handle the single-part
					//       case with two formatters, unless the root formatter is marked with
					//       "textFragments". We unpack here and chain the formatters ourselves.
					fnRootFormatter = vPropertySetting.formatter;
					vPropertySetting = vPropertySetting.parts[0];
					if (fnRootFormatter) {
						vPropertySetting.formatter
							= chain(fnRootFormatter, vPropertySetting.formatter);
					}
				}

				return vPropertySetting;
			}