function CLDR(oOptions) {
		if (!(this instanceof CLDR)) {
			return new CLDR(oOptions);
		}
		this._oOptions = oOptions;
		events.EventEmitter.call(this);
}