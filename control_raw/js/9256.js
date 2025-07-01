function (oPathValue) {
			var aPromises;

			// needed so that we can safely call the forEach
			Basics.expectType(oPathValue, "array");
			aPromises = oPathValue.value.map(function (oUnused, i) {
				// an embedded concat must use expression binding
				return Expression.parameter(oPathValue, i);
			});

			return SyncPromise.all(aPromises).then(function (aParameters) {
				var bExpression,
					aParts,
					oResult;

				bExpression = oPathValue.asExpression || aParameters.some(function (oParameter) {
					// if any parameter is type expression, the concat must become expression, too
					return oParameter.result === "expression";
				});
				// convert the results to strings after we know whether the result is expression
				aParts = aParameters.filter(function (oParameter) {
					// ignore null (otherwise the string 'null' would appear in expressions)
					return oParameter.type !== 'edm:Null';
				}).map(function (oParameter) {
					if (bExpression) {
						// the expression might have a lower operator precedence than '+'
						Expression.wrapExpression(oParameter);
					}

					return Basics.resultToString(oParameter, bExpression,
						oPathValue.complexBinding);
				});
				oResult = bExpression
					? {result : "expression", value : aParts.join("+")}
					: {result : "composite", value : aParts.join("")};
				oResult.type = "Edm.String";

				return oResult;
			});
		}