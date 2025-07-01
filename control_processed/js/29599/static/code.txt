function(err, info) {
					if(err) {
						return api.writeError(500, res, err);
					}
					return api.writeResponse(200, res, null, {"Severity":"Info","Message":"Confirmation email has been sent.","HttpCode":200,"BundleId":"org.eclipse.orion.server.core","Code":0});
				}