function (oPathValue, oParameters) {
			var oFunction = Basics.descend(oPathValue, "$Function", "string");

			switch (oFunction.value) {
				case "odata.concat": // 14.5.3.1.1 Function odata.concat
					return Expression.concat(oParameters);
				case "odata.fillUriTemplate": // 14.5.3.1.2 Function odata.fillUriTemplate
					return Expression.fillUriTemplate(oParameters);
				case "odata.uriEncode": // 14.5.3.1.3 Function odata.uriEncode
					return Expression.uriEncode(oParameters);
				default:
					return asyncError(oFunction, "unknown function: " + oFunction.value);
			}
		}