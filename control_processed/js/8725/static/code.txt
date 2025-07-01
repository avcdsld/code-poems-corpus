function () {
				var pInstanceCreation, oMsr = startMeasurements("_getInstance"),
					that = this;

				pInstanceCreation = new Promise(function (resolve, reject) {
					var oInstance;

					Log.debug("Cache Manager: Initialization...");
					if (!CacheManager._instance) {
						oInstance = that._findImplementation();

						Measurement.start(S_MSR_INIT_IMPLEMENTATION, "CM", S_MSR_CAT_CACHE_MANAGER);
						oInstance.init().then(resolveCacheManager, reject);
						Measurement.end(S_MSR_INIT_IMPLEMENTATION, "CM");
					} else {
						resolveCacheManager(CacheManager._instance);
					}
					function resolveCacheManager(instance) {
						CacheManager._instance = instance;
						oMsr.endAsync();
						Log.debug("Cache Manager initialized with implementation [" + CacheManager._instance.name + "], resolving _getInstance promise");
						resolve(instance);
					}
				});

				oMsr.endSync();
				return pInstanceCreation;
			}