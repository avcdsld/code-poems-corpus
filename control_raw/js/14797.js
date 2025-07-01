function onError(message, error) {
  // log the stack trace
  util.print_debug_error(error);

  // update error message
  try {
    error.message = message + ': ' + error.message;
  } catch(e) {}

  throw error;
}