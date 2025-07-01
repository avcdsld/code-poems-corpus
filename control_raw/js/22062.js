function removeInputValidator(inputId) {
  if (typeof inputId === 'string') {
      inputId = $(document.getElementById(inputId));
  }
  inputId.off('keyup').removeClass('validate-negative').removeClass('validate-positive');
}