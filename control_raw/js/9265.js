function (oPathValue, sType) {
			var sExpectedEdmType = sType === "And" || sType === "Or" ? "Edm.Boolean" : undefined;

			// Note: it is safe to modify the caller's object here
			oPathValue.complexBinding = false;

			return SyncPromise.all([
				Expression.parameter(oPathValue, 0, sExpectedEdmType),
				Expression.parameter(oPathValue, 1, sExpectedEdmType)
			]).then(function (aResults) {
				var bNeedsCompare,
					oParameter0 = aResults[0],
					oParameter1 = aResults[1],
					sSpecialType = "",
					sValue0,
					sValue1;

				if (oParameter0.type !== "edm:Null" && oParameter1.type !== "edm:Null") {
					oParameter0.category = mType2Category[oParameter0.type];
					oParameter1.category = mType2Category[oParameter1.type];
					Expression.adjustOperands(oParameter0, oParameter1);
					Expression.adjustOperands(oParameter1, oParameter0);

					if (oParameter0.category !== oParameter1.category) {
						error(oPathValue, "Expected two comparable parameters but instead saw "
							+ oParameter0.type + " and " + oParameter1.type);
					}
					switch (oParameter0.category) {
						case "Decimal":
							sSpecialType = ",'Decimal'";
							break;
						case "DateTimeOffset":
							sSpecialType = ",'DateTime'";
							break;
						// no default
					}
					bNeedsCompare = mTypeCategoryNeedsCompare[oParameter0.category];
				}
				sValue0 = Expression.formatOperand(oParameter0, !bNeedsCompare);
				sValue1 = Expression.formatOperand(oParameter1, !bNeedsCompare);
				return {
					result : "expression",
					type : "Edm.Boolean",
					value : bNeedsCompare
						? "odata.compare(" + sValue0 + "," + sValue1 + sSpecialType + ")"
							+ mOData2JSOperators[sType] + "0"
						: sValue0 + mOData2JSOperators[sType] + sValue1
				};
			});
		}