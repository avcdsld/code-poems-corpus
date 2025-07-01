function (oInterface, oPathValue) {
			var sBindingPath = oPathValue.value,
				oConstraints = {},
				oExclusiveAnnotation,
				oIsDigitSequence,
				oMinMaxAnnotation,
				oModel = oInterface.getModel(),
				oPathValueInterface = {
					getModel : function () {
						return oModel;
					},
					getPath : function () {
						return oPathValue.path;
					}
				},
				oProperty,
				oResult = {result : "binding", value : sBindingPath},
				oTarget;

			Basics.expectType(oPathValue, "string");

			// Note: "PropertyPath" is treated the same...
			oTarget = Basics.followPath(oPathValueInterface, {"Path" : sBindingPath});

			if (oTarget && oTarget.resolvedPath) {
				oProperty = oModel.getProperty(oTarget.resolvedPath);
				oResult.type = oProperty.type;
				switch (oProperty.type) {
				case "Edm.DateTime":
					oConstraints.displayFormat = oProperty["sap:display-format"];
					break;
				case "Edm.Decimal":
					if (oProperty.precision) {
						oConstraints.precision = oProperty.precision;
					}
					if (oProperty.scale) {
						oConstraints.scale = oProperty.scale;
					}
					oMinMaxAnnotation = oProperty["Org.OData.Validation.V1.Minimum"];
					if (oMinMaxAnnotation
							&& (oMinMaxAnnotation.Decimal || oMinMaxAnnotation.String)) {
						oConstraints.minimum =
							oMinMaxAnnotation.Decimal || oMinMaxAnnotation.String;
						oExclusiveAnnotation =
							oMinMaxAnnotation["Org.OData.Validation.V1.Exclusive"];
						if (oExclusiveAnnotation) {
							oConstraints.minimumExclusive = oExclusiveAnnotation.Bool || "true";
						}
					}
					oMinMaxAnnotation = oProperty["Org.OData.Validation.V1.Maximum"];
					if (oMinMaxAnnotation
							&& (oMinMaxAnnotation.Decimal || oMinMaxAnnotation.String)) {
						oConstraints.maximum =
							oMinMaxAnnotation.Decimal || oMinMaxAnnotation.String;
						oExclusiveAnnotation =
							oMinMaxAnnotation["Org.OData.Validation.V1.Exclusive"];
						if (oExclusiveAnnotation) {
							oConstraints.maximumExclusive = oExclusiveAnnotation.Bool || "true";
						}
					}
					break;
				case "Edm.String":
					oConstraints.maxLength = oProperty.maxLength;
					oIsDigitSequence = oProperty["com.sap.vocabularies.Common.v1.IsDigitSequence"];
					if (oIsDigitSequence) {
						oConstraints.isDigitSequence = oIsDigitSequence.Bool || "true";
					}
					break;
				// no default
				}
				if (oProperty.nullable === "false") {
					oConstraints.nullable = "false";
				}
				oResult.constraints = oConstraints;
			} else {
				Log.warning("Could not find property '" + sBindingPath + "' starting from '"
					+ oPathValue.path + "'", null, sAnnotationHelper);
			}

			return oResult;
		}