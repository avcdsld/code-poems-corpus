function Op(o,l,r){
	// set expression yes, no?
	this._expression = false;
	this._traversed = false;
	this._parens = false;
	this._cache = null;
	this._invert = false;
	this._opToken = o;
	this._op = o && o._value || o;
	
	if (this._op == 'and') {
		this._op = '&&';
	} else if (this._op == 'or') {
		this._op = '||';
	} else if (this._op == 'is') {
		this._op = '===';
	} else if (this._op == 'isnt') {
		this._op = '!==';
	};
	
	
	this._left = l;
	this._right = r;
	return this;
}