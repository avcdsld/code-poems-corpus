function(node) {
        	            var globalScope = context.getScope();

        	            globalScope.through.forEach(function(ref) {
    	            	    if (isRecoveredNode(ref.identifier)) {
    	            	    	return;
    	            	    }
        	                var variable = getDeclaredGlobalVariable(globalScope, ref),
        	                    name = ref.identifier.name;
        	                if (!variable) {
        	                	// Check if Tern knows about a definition in another file
        	                	var env = Finder.findESLintEnvForMember(name);
        	                    var tern = context.getTern();
								var query = {end: ref.identifier.start};
								var foundType = null;
								var expr = tern.findQueryExpr(tern.file, query);
								if (!expr) {
									return;
								}
								var type = tern.findExprType(query, tern.file, expr);
								// The origin could be a primitive in the same file (a=1;) which we still want to mark
								if (type && (type.originNode || Array.isArray(type.types) && type.types.length > 0) && type.origin && type.origin !== tern.file.name){
									foundType = type;
								}
            	                if (!foundType){
            	                    var inenv = env ? '-inenv' : ''; //$NON-NLS-1$
            	                    var nls = 'no-undef-defined'; //$NON-NLS-1$
            	                    context.report(ref.identifier, ProblemMessages['no-undef-defined'], {0:name, nls: nls, pid: nls+inenv, data: name});
        	                    }
        	                }
        	            });
                    }