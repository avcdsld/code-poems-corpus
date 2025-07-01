function(ruleConfig) {

			var severity = Array.isArray(ruleConfig) ? ruleConfig[0] : ruleConfig;

			if (typeof severity === "string") {
				severity = RULE_SEVERITY[severity.toLowerCase()] || 0;
			}

			return typeof severity === "number" && severity === 2;
		}