function(path) {
            if (!path.inList) {
              return;
            }

            const { node } = path;
            if (node.kind !== "var") {
              return;
            }

            const next = path.getSibling(path.key + 1);
            if (!next.isForStatement()) {
              return;
            }

            const init = next.get("init");
            if (!init.isVariableDeclaration({ kind: node.kind })) {
              return;
            }

            const declarations = node.declarations.concat(
              init.node.declarations
            );

            // temporary workaround to forces babel recalculate scope,
            // references and binding until babel/babel#4818 resolved
            path.remove();
            init.replaceWith(t.variableDeclaration("var", declarations));
          }