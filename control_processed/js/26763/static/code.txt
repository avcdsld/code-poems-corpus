function getDependencies(node, name, locals) {
      var deps = [];

      if (!locals) {
        locals = [];
      }

      function log() {
        if (name === 'xxx') {
          console.log.apply(null, [name + ':'].concat(Array.prototype.slice.call(arguments, 0)));
        }
      }

      function pushLocal(loc) {
        if (locals.indexOf(loc) === -1) {
          log('PUSHING LOCAL', loc);
          locals.push(loc);
        }
      }

      function pushDependency(dep) {
        if (deps.indexOf(dep) === -1) {
          log('PUSHING DEPENDENCY', dep);
          deps.push(dep);
        }
      }

      function pushDependencies(arr) {
        arr.forEach(pushDependency);
      }

      function getLocals(nodes) {
        return nodes.map(function(id) {
          return id.name;
        });
      }

      function walk(nodes) {
        if (!nodes) {
          return;
        }
        if (nodes.type) nodes = [nodes];
        nodes.forEach(processNode);
      }

      function processNode(node) {
        log('PROCESSING:', node.type);
        switch(node.type) {
          case 'Identifier':
            pushDependency(node.name);
            return;
          case 'VariableDeclarator':
            pushLocal(node.id.name);
            walk(node.init);
            return;
          case 'FunctionDeclaration':
            pushLocal(node.id.name);
            // Recursively get this function's local dependencies.
            // so that flat locals don't clobber them.
            pushDependencies(getDependencies(node.body, name, getLocals(node.params)));
            return;
          case 'FunctionExpression':
            // Recursively get this function's local dependencies.
            // so that flat locals don't clobber them.
            pushDependencies(getDependencies(node.body, name, getLocals(node.params)));
            return;
          case 'CatchClause':
            pushLocal(node.param);
            walk(node.body);
            return;
          case 'MemberExpression':
            walk(node.object);
            // If the MemberExpression is computed syntax (a[b]) then
            // the property value may be a depencency, so step in.
            if (node.computed) walk(node.property);
            return;
          case 'ExpressionStatement':
            walk(node.expression);
            return;
          case 'SequenceExpression':
            walk(node.expressions);
            return;
          case 'SwitchStatement':
            walk(node.discriminant);
            walk(node.cases);
            return;
          case 'ObjectExpression':
            walk(node.properties);
            return;
          case 'ArrayExpression':
            walk(node.elements);
            return;
          case 'TryStatement':
            walk(node.block);
            walk(node.handler);
            walk(node.finalizer);
            return;
          case 'BlockStatement':
            walk(node.body);
            return;
          case 'ForStatement':
            walk(node.init);
            walk(node.test);
            walk(node.update);
            walk(node.body);
            return;
          case 'ForInStatement':
            walk(node.left);
            walk(node.right);
            walk(node.body);
            return;
          case 'WhileStatement':
            walk(node.test);
            walk(node.body);
            return;
          case 'DoWhileStatement':
            walk(node.body);
            walk(node.test);
            return;
          case 'VariableDeclaration':
            walk(node.declarations);
            return;
          case 'Property':
            walk(node.value);
            return;
          case 'NewExpression':
          case 'CallExpression':
            walk(node.callee);
            walk(node.arguments);
            return;
          case 'SwitchCase':
          case 'IfStatement':
          case 'ConditionalExpression':
            walk(node.test);
            walk(node.consequent);
            walk(node.alternate);
            return;
          case 'BinaryExpression':
          case 'LogicalExpression':
          case 'AssignmentExpression':
            walk(node.left);
            walk(node.right);
            return;
          case 'ThrowStatement':
          case 'ReturnStatement':
          case 'UnaryExpression':
          case 'UpdateExpression':
            walk(node.argument);
            return;
          case 'Literal':
          case 'EmptyStatement':
          case 'ThisExpression':
          case 'BreakStatement':
          case 'ContinueStatement':
            // Pass on literals, {}, this, break, continue
            return;
          default:
            console.log(node);
            throw new Error('Unknown Node: ' + node.type);
        }
      }

      function isValidDependency(d) {
        // Remove any local variables, whitelisted tokens like "arguments" or "NaN",
        // and anything in the global scope. Cheating a bit here by using the node
        // global scope instead of a ton of whitelisted tokens.
        return locals.indexOf(d) === -1 && !global[d] && WHITELISTED.indexOf(d) === -1;
      }

      walk(node);
      return deps.filter(isValidDependency);
    }