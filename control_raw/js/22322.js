function processCreateElement (maybeReactComponent, args, file, path, types) {
  // If the first argument is a string (built-in React component), return
  if (maybeReactComponent.type === 'StringLiteral') return

  if (!file.insertedVueraImport) {
    file.path.node.body.unshift(
      types.importDeclaration(
        [
          types.importSpecifier(
            types.identifier('__vueraReactResolver'),
            types.identifier('__vueraReactResolver')
          ),
        ],
        types.stringLiteral('vuera')
      )
    )
  }
  // Prevent duplicate imports
  file.insertedVueraImport = true

  // Replace React.createElement(component, props) with our helper function
  path.replaceWith(
    types.callExpression(types.identifier('__vueraReactResolver'), [maybeReactComponent, ...args])
  )
}