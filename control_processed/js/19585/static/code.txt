function(eventName, successArgs, skip) {
		"use strict";

		if ((arguments.length === 3 && skip) || this.options[eventName] === null) {
			return true;
		}

		if (typeof this.options[eventName] === "function") {
			if (typeof successArgs === "function") {
				successArgs = successArgs();
			}
			return this.options[eventName].apply(this, successArgs);
		} else {
			console.log("Provided callback for " + eventName + " is not a function.");
			return false;
		}
	}