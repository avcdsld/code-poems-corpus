function(){
					if(_isActive) return;

					_hash = _getWindowHash();

					//thought about branching/overloading hasher.init() to avoid checking multiple times but
					//don't think worth doing it since it probably won't be called multiple times.
					if(_isHashChangeSupported){
						_addListener(window, 'hashchange', _checkHistory);
					}else {
						if(_isLegacyIE){
							if(! _frame){
								_createFrame();
							}
							_updateFrame();
						}
						_checkInterval = setInterval(_checkHistory, POOL_INTERVAL);
					}

					_isActive = true;
					hasher.initialized.dispatch(_trimHash(_hash));
				}