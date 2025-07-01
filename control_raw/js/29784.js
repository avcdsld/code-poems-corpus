function(deferred, message, avoidDisplayError){
				this._serviceRegistry.getService("orion.page.message").showWhile(deferred, message); //$NON-NLS-1$

				var that = this;
				// If the underlying deferred was rejected, display an error
				deferred.then(null, function(error) {
					if (avoidDisplayError) {
						// do nothing
					} else {
						that.setProgressResult(error);
					}
				});
				return this.progress(deferred, message);
			}