function getReactProps(node, parent) {
  if (node.openingElement.attributes.length === 0 ||
  htmlElements.indexOf(node.openingElement.name.name) > 0) return {};
  const result = node.openingElement.attributes
    .map(attribute => {
      const name = attribute.name.name;
      let valueName;
      if (attribute.value === null) valueName = undefined;
      else if (attribute.value.type === 'Literal') valueName = attribute.value.value;
      else if (attribute.value.expression.type === 'Literal') {
        valueName = attribute.value.expression.value;
      } else if (attribute.value.expression.type === 'Identifier') {
        valueName = attribute.value.expression.name;
      } else if (attribute.value.expression.type === 'CallExpression') {
        valueName = attribute.value.expression.callee.object.property.name;
      } else if (attribute.value.expression.type === 'BinaryExpression') {
        valueName = attribute.value.expression.left.name
          + attribute.value.expression.operator
          + (attribute.value.expression.right.name
          || attribute.value.expression.right.value);
      } else if (attribute.value.expression.type === 'MemberExpression') {
        let current = attribute.value.expression;
        while (current && current.property) {
          //  && !current.property.name.match(/(state|props)/)
          valueName = `.${current.property.name}${valueName || ''}`;
          current = current.object;
          if (current.type === 'Identifier') {
            valueName = `.${current.name}${valueName || ''}`;
            break;
          }
        }
        valueName = valueName.replace('.', '');
      } else if (attribute.value.expression.type === 'LogicalExpression') {
        valueName = attribute.value.expression.left.property.name;
        // valueType = attribute.value.expression.left.object.name;
      } else if (attribute.value.expression.type === 'JSXElement') {
        const nodez = attribute.value.expression;
        const output = {
          name: nodez.openingElement.name.name,
          children: getChildJSXElements(nodez, parent),
          props: getReactProps(nodez, parent),
          state: {},
          methods: [],
        };
        valueName = output;
      } else valueName = escodegen.generate(attribute.value);

      return {
        name,
        value: valueName,
        parent,
      };
    });
  return result;
}