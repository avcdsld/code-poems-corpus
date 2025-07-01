function reason(node) {
  if (isAudioVideoWithControls(node)) {
    return `an <${node.tag}> element with the \`controls\` attribute`;
  }

  if (!ast.isElementNode(node) && !ast.isComponentNode(node)) {
    return null;
  }

  if (isHiddenInput(node)) {
    return null;
  }

  if (INTERACTIVE_TAG_NAMES.indexOf(node.tag) > -1) {
    return `<${node.tag}>`;
  }

  let role = getInteractiveAriaRole(node);
  if (role) {
    return `an element with \`${role}\``;
  }

  if (isHyperLink(node)) {
    return 'an <a> element with the `href` attribute';
  }

  if (ast.hasAttribute(node, 'tabindex')) {
    return 'an element with the `tabindex` attribute';
  }

  if ((node.tag === 'img' || node.tag === 'object') && ast.hasAttribute(node, 'usemap')) {
    return `an <${node.tag}> element with the \`usemap\` attribute`;
  }

  return null;
}