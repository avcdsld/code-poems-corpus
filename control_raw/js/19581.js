function(value) {
		"use strict";

		if (!Array.isArray(value)) {
			value = [value];
		}

		return value.map(function(data) {
			if (data === "now") {
				return new Date();
			}
			if (data instanceof Date) {
				return data;
			}
			return false;
		}).filter(function(d) { return d !== false; });
	}