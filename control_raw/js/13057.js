function Root(body,opts){
	this._traversed = false;
	this._body = AST.blk(body);
	this._scope = new RootScope(this,null);
	this._options = {};
}