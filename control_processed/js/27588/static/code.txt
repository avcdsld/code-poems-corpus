function traverse ({ seq, node, context, numChildren, parent }) {
  if (node === undefined || node === true) {
    return;
  }

  if (node === false) {
    if (parent && isFunction(parent.type)) {
      emitEmpty(seq);
      return;
    } else {
      return;
    }
  }

  if (node === null) {
    emitEmpty(seq);
    return;
  }

  switch (typeof node) {
  case "string": {
    // Text node.
    emitText({
      seq,
      text: htmlStringEscape(node),
      numChildren,
      isNewlineEatingTag: Boolean(parent && newlineEatingTags[parent.type])
    });

    return;
  }
  case "number": {
    emitText({
      seq,
      text: node.toString(),
      numChildren
    });

    return;
  }
  case "object": {
    if (node.__prerendered__) {
      evalPreRendered(seq, node, context);
      return;
    } else if (typeof node.type === "string") {
      // Plain-jane DOM element, not a React component.
      seq.delegateCached(node, (_seq, _node) => renderNode(_seq, _node, context));
      return;
    } else if (node.$$typeof) {
      // React component.
      seq.delegateCached(node, (_seq, _node) => evalComponent(_seq, _node, context));
      return;
    }
  }
  }

  throw new TypeError(`Unknown node of type: ${node.type}`);
}