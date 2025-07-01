function(fn, state) {
			state = utils.extend({amount: 0, found: 0}, state || {});

			if (typeof fn !== 'function') {
				var elemName = fn.toLowerCase();
				fn = function(item) {return item.name().toLowerCase() == elemName;};
			}
				
			var result = [];
			this.children.forEach(function(child) {
				if (fn(child)) {
					result.push(child);
					state.found++;
					if (state.amount && state.found >= state.amount) {
						return;
					}
				}
				
				result = result.concat(child.findAll(fn));
			});
			
			return result.filter(function(item) {
				return !!item;
			});
		}