function(context) {
        		return {
        			/* @callback */
        			'VariableDeclarator': function(node) {
        				if(node.init && node.init.type === 'Identifier' && node.init.name === 'undefined') {
    						context.report(node.init, ProblemMessages['no-undef-init']);
        				}
        			}
        		};
        }