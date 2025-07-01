function(node) {
						var returnInfo = functions[functions.length - 1];
						var returnTypeDefined = "type" in returnInfo;
			
						if (returnTypeDefined) {
							var typeOfReturnStatement = getValue(node);
							var storeType = returnInfo.type;
							if (storeType !== typeOfReturnStatement) {
								// "null" and "object", "string" or String" are compatible
								switch(storeType) {
									case "null" :
										if (typeOfReturnStatement !== "object" && typeOfReturnStatement !== "String" && typeOfReturnStatement !== "string") {
											context.report(node, ProblemMessages['inconsistent-return'], {type1: storeType, type2: typeOfReturnStatement});
										}
										break;
									case "String" :
									case "string" :
										if (typeOfReturnStatement !== "null") {
											context.report(node, ProblemMessages['inconsistent-return'], {type1: storeType, type2: typeOfReturnStatement});
										}
										break;
									case "object" :
										if (typeOfReturnStatement !== "null") {
											context.report(node, ProblemMessages['inconsistent-return'], {type1: storeType, type2: typeOfReturnStatement});
										}
										break;
									default:
										context.report(node, ProblemMessages['inconsistent-return'], {type1: storeType, type2: typeOfReturnStatement});
								}
							}
						} else {
							returnInfo.type = getValue(node);
						}
					}