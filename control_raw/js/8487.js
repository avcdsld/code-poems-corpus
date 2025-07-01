function analyzeModuleDefinition(node) {
	var args = node.arguments;
	var arg = 0;
	if ( arg < args.length
		 && args[arg].type === Syntax.Literal && typeof args[arg].value === 'string' ) {
		warning("module explicitly defined a module name '" + args[arg].value + "'");
		currentModule.name = args[arg].value;
		arg++;
	}
	if ( arg < args.length && args[arg].type === Syntax.ArrayExpression ) {
		currentModule.dependencies = convertValue(args[arg], "string[]");
		arg++;
	}
	if ( arg < args.length && args[arg].type === Syntax.FunctionExpression ) {
		currentModule.factory = args[arg];
		arg++;
	}
	if ( currentModule.dependencies && currentModule.factory ) {
		for ( var i = 0; i < currentModule.dependencies.length && i < currentModule.factory.params.length; i++ ) {
			var name = currentModule.factory.params[i].name;
			var module = resolveModuleName(currentModule.module, currentModule.dependencies[i]);
			debug("  import " + name + " from '" + module + "'");
			currentModule.localNames[name] = {
				module: module
				// no (or empty) path
			};
		}
	}
	if ( currentModule.factory ) {
		collectShortcuts(currentModule.factory.body);
	}
}