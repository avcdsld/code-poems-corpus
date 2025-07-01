function getConstructorInterface(namespace, module) {

    var methods = [];


    // Add the main chainable type.

    var chainableGenerics = getChainableBaseGenerics(namespace.name)
    var chainableType = 'ChainableBase' + chainableGenerics;

    if (namespace.name !== 'Object') {
      chainableType += ' & Object.ChainableBase' + getChainableBaseGenerics('Object');
    }
    module.types.push({
      name: 'Chainable' + chainableGenerics,
      type: chainableType
    });


    // Set up constructor methods.

    var rawType = getRawType(namespace.name);

    var constructorMethod = {
      name: 'new',
      type: 'constructor',
      module: namespace.name,
      generics: getNamespaceBaseGenerics(namespace.name),
      returns: 'Chainable' + getChainableInstanceGenerics(namespace.name),
      params: [{
        name: 'raw',
        type: rawType
      }]
    };

    var createMethod = namespace.methods.find(function(method) {
      return method.name === 'create';
    });

    if (createMethod) {
      // If the namespace has a "create" method, then it will be mapped
      // to the chainable constructor, so accomodate for that here.
      constructorMethod.params = createMethod.params;
      constructorMethod.params[0].required = false;
    }

    var factoryMethod = clone(constructorMethod);
    factoryMethod.name = '';

    methods.push(constructorMethod);
    methods.push(factoryMethod);


    // Set up all remaining methods.

    namespace.methods.forEach(function(method) {
      var instanceParam = {
        name: 'instance',
        required: true,
        type: getInstanceParamType(method, rawType)
      };
      var method = clone(method);
      if (method.type === 'instance') {
        method.params.unshift(instanceParam);
        if (method.signatures) {
          method.signatures.forEach(function(signature) {
            signature.unshift(instanceParam);
          });
        }
        if (namespace.name === 'Array') {
          method.generics = ['T'];
        }
      }
      methods.push(method);
    });

    methods = buildMethods(methods, namespace, 'static');
    return getInterfaceSource('Constructor', methods.join('\n'), null, 'SugarNamespace');
  }