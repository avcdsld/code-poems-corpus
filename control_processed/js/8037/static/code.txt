function RenderContext() {
		this._aBuffer = [];
		var that = this;
		this.add = function() {
			that._aBuffer.push.apply(that._aBuffer, arguments);
		};
		this.addWithParam = function(s, o) {
			for (var n in o) {
				var reg = new RegExp("\{" + n + "\}","g");
				s = s.replace(reg,o[n]);
			}
			that.add(s);
		};
		this.toString = function() {
			return that._aBuffer.join("");
		};
	}