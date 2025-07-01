function formatComment(comment) {
  if (!comment) {
    return undefined;
  }
  const parts = comment.trim().split('\n');
  if (parts.length === 1 && parts[0].indexOf('*') !== 0) {
    return parts[0];
  }
  return parts.reduce((previousValue, currentValue) => {
    // newlines in the middle of the comment should stay to achieve:
    // multiline comments entered by user drive unchanged from JDL
    // studio to generated domain class
    let delimiter = '';
    if (previousValue !== '') {
      delimiter = '\n';
    }
    return previousValue.concat(delimiter, currentValue.trim().replace(/[*]*\s*/, ''));
  }, '');
}