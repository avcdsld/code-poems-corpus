function(oPromise) {
					// In order to make the error handling of the Promise.all() happen after all Promises finish, we catch all rejected Promises and make them resolve with an marked object.
					oPromise = oPromise.then(
						function(v) {
							return {
								result: v,
								rejected: false
							};
						},
						function(v) {
							return {
								result: v,
								rejected: true
							};
						}
					);
					return oPromise;
				}