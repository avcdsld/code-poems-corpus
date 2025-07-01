function(fn, options) {
			// TODO hack for stable sort, remove after fixing `list()`
			var order = this._list.length;
			if (options && 'order' in options) {
				order = options.order * 10000;
			}
			this._list.push(utils.extend({}, options, {order: order, fn: fn}));
		}