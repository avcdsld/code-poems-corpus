function(name, value) {
			var prefs = name;
			if (typeof name === 'string') {
				prefs = {};
				prefs[name] = value;
			}
			
			Object.keys(prefs).forEach(function(k) {
				var v = prefs[k];
				if (!(k in defaults)) {
					throw new Error('Property "' + k + '" is not defined. You should define it first with `define` method of current module');
				}
				
				// do not set value if it equals to default value
				if (v !== defaults[k].value) {
					// make sure we have value of correct type
					switch (typeof defaults[k].value) {
						case 'boolean':
							v = toBoolean(v);
							break;
						case 'number':
							v = parseInt(v + '', 10) || 0;
							break;
						default: // convert to string
							if (v !== null) {
								v += '';
							}
					}

					preferences[k] = v;
				} else if (k in preferences) {
					delete preferences[k];
				}
			});
		}