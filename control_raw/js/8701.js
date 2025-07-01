function chain(fnAfter, fnBefore) {
			if (!fnBefore) {
				return fnAfter;
			}

			function formatter() {
				return fnAfter.call(this, fnBefore.apply(this, arguments));
			}
			return formatter;
		}