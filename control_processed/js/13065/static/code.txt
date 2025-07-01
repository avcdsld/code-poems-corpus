function Assign(o,l,r){
	
	// workaround until we complete transition from lua-style assignments
	// to always use explicit tuples - then we can move assignments out etc
	// this will not be needed after we remove support for var a,b,c = 1,2,3
	if ((l instanceof VarReference) && (l.value() instanceof Arr)) {
		// converting all nodes to var-references ?
		// do we need to keep it in a varblock at all?
		var vars = l.value().nodes().map(function(v) {
			// what about inner tuples etc?
			// keep the splats -- clumsy but true
			var v_;
			if (v instanceof Splat) {
				if (!((v.value() instanceof VarReference))) { (v.setValue(v_ = new VarReference(v.value(),l.type())),v_) };
			} else if (v instanceof VarReference) {
				true;
			} else {
				// what about retaining location?
				// v = v.value if v isa VarOrAccess
				v = new VarReference(v,l.type());
			};
			
			return v;
			
			// v isa VarReference ? v : VarReference.new(v)
		});
		
		return new TupleAssign(o,new Tuple(vars),r);
	};
	
	if (l instanceof Arr) {
		return new TupleAssign(o,new Tuple(l.nodes()),r);
	};
	
	// set expression yes, no?
	this._expression = false;
	this._traversed = false;
	this._parens = false;
	this._cache = null;
	this._invert = false;
	this._opToken = o;
	this._op = o && o._value || o;
	this._left = l;
	this._right = r;
	return this;
}