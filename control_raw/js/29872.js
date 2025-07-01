function collectUnusedVariables(scope, unusedVars) {
	            var variables = scope.variables;
	            var childScopes = scope.childScopes;
	            var i, l;
	            if (scope.type !== "TDZ" && (scope.type !== "global" || config.vars === "all")) {
	                for (i = 0, l = variables.length; i < l; ++i) {
	                    var variable = variables[i];
	
	                    // skip a variable of class itself name in the class scope
	                    if (scope.type === "class" && scope.block.id === variable.identifiers[0]) {
	                        continue;
	                    }
	
	                    // skip function expression names and variables marked with markVariableAsUsed()
	                    if (scope.functionExpressionScope || variable.eslintUsed) {
	                        continue;
	                    }
	
	                    // skip implicit "arguments" variable
	                    if (scope.type === "function" && variable.name === "arguments" && variable.identifiers.length === 0) {
	                        continue;
	                    }
	
	                    // explicit global variables don't have definitions.
	                    var def = variable.defs[0];
	
	                    if (def) {
	                        var type = def.type;
	                        // skip catch variables
	                        if (type === "CatchClause") {
	                            if (config.caughtErrors === "none") {
	                                continue;
	                            }
	
	                            // skip ignored parameters
	                            if (config.caughtErrorsIgnorePattern && config.caughtErrorsIgnorePattern.test(def.name.name)) {
	                                continue;
	                            }
	                        }
	                        if (type === "Parameter") {
	                            // skip any setter argument
	                            if (def.node.parent.type === "Property" && def.node.parent.kind === "set") {
	                                continue;
	                            }
	
	                            // if "args" option is "none", skip any parameter
	                            if (config.args === "none") {
	                                continue;
	                            }
	
	                            // skip ignored parameters
	                            if (config.argsIgnorePattern && config.argsIgnorePattern.test(def.name.name)) {
	                                continue;
	                            }
	
	                            // if "args" option is "after-used", skip all but the last parameter
	                            if (config.args === "after-used" && def.index < def.node.params.length - 1) {
	                                continue;
	                            }
	                        } else {
	                            // skip ignored variables
	                            if (config.varsIgnorePattern && config.varsIgnorePattern.test(def.name.name)) {
	                                continue;
	                            }
	                        }
	                        if (def.node.type === 'VariableDeclarator') {
				        		// Variables can be marked as 'exported' in a comment if they are used as global variables
								var comments = def.parent.leadingComments;
								var report = true;
								if (Array.isArray(comments)) {
									for (var k = 0, len = comments.length; k < len; k++) {
										if (comments[k].type === "Block" && comments[k].value.toLowerCase().indexOf('exported') >= 0){ //$NON-NLS-1$
											report = false;
											break;
										}
									}
								}
								if (!report) {
									continue;
								}
							}
	                    }
	                    if (!isUsedVariable(variable) && !isExported(variable)) {
	                    	if(def) {
	                    		type = def.type;
	                    		variable.data = {
		                    		0: variable.identifiers[0].name,
		                    		nls: 'no-unused-vars-unused',
		                    		pid: 'no-unused-vars-unused'
		                    	};
		                    	if(type === "Parameter") {
		                    		continue;
		                    	}
		                    	if(type === "ImportBinding") {
		                    		variable.data.pid = 'no-unused-vars-import';
		                    	} else if(def.node.type === "FunctionDeclaration") {
		                    		var tern = context.getTern();
		                    		var refQuery = {
		                    			end: def.node.id.start
		                    		};
		                    		var filename = tern.file.name;
		                    		var refs = tern.findRefs(refQuery, tern.file);
		                    		var result = [];
		                    		if (refs && Array.isArray(refs.refs)) {
		                    			// filtering the refs from the current file - remove the one that matches the current node
		                    			refs.refs.forEach(function(match) {
		                    				if (match.file !== filename) {
		                    					// any match in a different file is a good match
		                    					result.push(match);
		                    				}
		                    			});
		                    		}
		                    		if (result.length > 0) {
		                    			continue;
		                    		}
		                    		variable.data.pid = variable.data.nls = 'no-unused-vars-unused-funcdecl';
		                    	} else if(typeof variable.isread === "boolean" && !variable.isread) {
		                    		variable.data.pid = variable.data.nls = 'no-unused-vars-unread';
		                    	}
	                    	}
	                        unusedVars.push(variable);
	                    }
	                }
	            }
	            for (i = 0, l = childScopes.length; i < l; ++i) {
	                collectUnusedVariables(childScopes[i], unusedVars);
	            }
	            return unusedVars;
	        }