function canFocus(element) {
  return (
    !!element &&
    element.getAttribute('tabindex') !== '-1' &&
    !element.hasAttribute('disabled') &&
    (
      element.hasAttribute('tabindex') ||
      element.hasAttribute('href') ||
      element.isContentEditable ||
      ['INPUT', 'SELECT', 'BUTTON', 'TEXTAREA', 'VIDEO', 'AUDIO'].indexOf(element.nodeName) !== -1
    )
  );
}