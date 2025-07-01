function createError(name, options)
{
  // TODO: validate that name is a string and options is an object

  // TODO: this code is a bit of a mess and needs to be cleaned up

  // create a new error
  var error = new Error();

  // set its name
  error.name = name;

  // set the error code
  var code;
  error.code = code = options.code;

  // if no error message was specified in the options
  var message = options.message;
  if (!message)
  {
    // use the error code to get the error message template
    var messageTemplate = errorMessages[code];

    // if some error message arguments were specified, substitute them into the
    // error message template to get the full error message, otherwise just use
    // the error message template as the error message
    var messageArgs = options.messageArgs;
    if (messageArgs)
    {
      messageArgs = messageArgs.slice();
      messageArgs.unshift(messageTemplate);
      message = Util.format.apply(Util, messageArgs);
    }
    else
    {
      message = messageTemplate;
    }
  }
  error.message = message;

  // if no sql state was specified in the options, use the error code to try to
  // get the appropriate sql state
  var sqlState = options.sqlState;
  if (!sqlState)
  {
    sqlState = errCodeToSqlState[code];
  }
  error.sqlState = sqlState;

  // set the error data
  error.data = options.data;

  // set the error response and response body
  error.response     = options.response;
  error.responseBody = options.responseBody;

  // set the error cause
  error.cause = options.cause;

  // set the error's fatal flag
  error.isFatal = options.isFatal;

  // if the error is not synchronous, add an externalize() method
  if (!options.synchronous)
  {
    error.externalize = function(errorCode, errorMessageArgs, sqlState)
    {
      var propNames =
      [
        'name',
        'code',
        'message',
        'sqlState',
        'data',
        'response',
        'responseBody',
        'cause',
        'isFatal',
        'stack'
      ];

      var externalizedError = new Error();

      var propName, propValue;
      for (var index = 0, length = propNames.length; index < length; index++)
      {
        propName = propNames[index];
        propValue = this[propName];
        if (Util.exists(propValue))
        {
          externalizedError[propName] = propValue;
        }
      }

      return externalizedError;
    };
  }

  return error;
}