function onlyProgressBar(props, propName, componentName) {
  const children = props[propName];
  if (!children) {
    return null;
  }

  let error = null;

  React.Children.forEach(children, child => {
    if (error) {
      return;
    }

    /**
     * Compare types in a way that works with libraries that patch and proxy
     * components like react-hot-loader.
     *
     * see https://github.com/gaearon/react-hot-loader#checking-element-types
     */
    const element = <DecoratedProgressBar />;
    if (child.type === element.type) return;

    const childIdentifier = React.isValidElement(child)
      ? child.type.displayName || child.type.name || child.type
      : child;
    error = new Error(
      `Children of ${componentName} can contain only ProgressBar ` +
        `components. Found ${childIdentifier}.`,
    );
  });

  return error;
}