function (vRawValue, oDetails) {
				var sPath = oDetails.context.getPath();

				if (sPath.slice(-1) === "/") {
					// cut off trailing slash, happens with computed annotations
					sPath = sPath.slice(0, -1);
				}
				return Expression.getExpression({
						asExpression : false,
						complexBinding : false,
						model : oDetails.context.getModel(),
						path : sPath,
						prefix : "",
						value : vRawValue,
						$$valueAsPromise : oDetails.$$valueAsPromise
					});
			}