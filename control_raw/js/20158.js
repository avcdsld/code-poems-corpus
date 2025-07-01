function isRenderMethod (props) {
    return props.some((prop) => {
      return prop.key.name === 'key' && prop.value.value === 'render'
    }) && props.some((prop) => {
      return prop.key.name === 'value' && t.isFunctionExpression(prop.value)
    })
  }