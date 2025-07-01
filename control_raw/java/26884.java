@RequestMapping(value = "/scope", method = GET, produces = APPLICATION_JSON_VALUE)
	public List<Scope> allScopes() {
		return this.scopeService.getAllScopes();
	}