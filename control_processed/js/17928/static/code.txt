function transform(el, context) {
    const replacement = context.createNodeForEl(
        el.tagName.replace(/^(ebay-.*)\-(?=[^-]*$)/, '$1:'),
        el.getAttributes()
    );
    replacement.body = replacement.makeContainer(el.body.items);
    el.replaceWith(replacement);
}