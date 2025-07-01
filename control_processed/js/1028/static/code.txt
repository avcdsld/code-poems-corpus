function createPropsPrototype(props, parentProps, propTypes, componentClass) {
  const defaultProps = Object.create(null);

  Object.assign(defaultProps, parentProps, props);

  // Avoid freezing `id` prop
  const id = getComponentName(componentClass);
  delete props.id;

  // Add getters/setters for async prop properties
  Object.defineProperties(defaultProps, {
    // `id` is treated specially because layer might need to override it
    id: {
      configurable: false,
      writable: true,
      value: id
    }
  });

  // Add getters/setters for async prop properties
  addAsyncPropsToPropPrototype(defaultProps, propTypes);

  return defaultProps;
}