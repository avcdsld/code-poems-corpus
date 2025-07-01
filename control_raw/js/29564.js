function run(server, query) {
			if(server.options && typeof server.options.plugins === 'object') {
				var plugins = server.options.plugins;
				var keys = Object.keys(plugins);
				var envs = Object.create(null);
				for(var i = 0; i < keys.length; i++) {
					var key = keys[i];
					var env = plugins[key].env;
					if(env) {
						envs[env] = true;
					} else {
						envs[plugins[key]] = true;
					}
				}
				return envs;
			}
			return null;
		}