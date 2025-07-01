function(load) {
			var value, loading, handles = [],
				h;
			return function(handle) {
				if(!loading) {
					loading = true;
					load(function(v) {
						value = v;
						while(h = handles.shift()) {
							try {
								h && h.apply(null, [value]);
							} catch(e) {
								setTimeout(function() {
									throw e;
								}, 0)
							}
						}
					})
				}
				if(value) {
					handle && handle.apply(null, [value]);
					return value;
				}
				handle && handles.push(handle);
				return value;
			}
		}