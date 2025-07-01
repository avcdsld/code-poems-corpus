function(sProperty, vGetter, aArgs, caller) {
			if (!vGetter) {
				return;
			}

			if (!caller) {
				caller = this;
			}

			Object.defineProperty(this, sProperty, {
				configurable: true,
				get: function() {
					if (this._mCustomPropertyBag[sProperty]) {
						return this._mCustomPropertyBag[sProperty];
					}

					if (!this._mPropertyBag.hasOwnProperty(sProperty)) {
						this._mPropertyBag[sProperty] = new SyncPromise(function(resolve, reject) {
						if (typeof vGetter == 'function') {
								resolve(vGetter.apply(caller, aArgs));
						} else {
								resolve(vGetter);
						}
						});

					}

					return this._mPropertyBag[sProperty];
				},
				set: function(vValue) {
					this._mCustomPropertyBag[sProperty] = vValue;
				}
			});
		}