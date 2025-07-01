function parseVendors(data) {
		var out = {};
		Object.keys(data.agents).forEach(function(name) {
			var agent = data.agents[name];
			out[name] = {
				prefix: agent.prefix,
				versions: agent.versions
			};
		});
		return out;
	}