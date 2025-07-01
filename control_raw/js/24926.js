function validateRSAA(action) {
  var validationErrors = [];
  const validCallAPIKeys = [
    'endpoint',
    'options',
    'method',
    'body',
    'headers',
    'credentials',
    'bailout',
    'types',
    'fetch',
    'ok'
  ];
  const validMethods = [
    'GET',
    'HEAD',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
  ];
  const validCredentials = ['omit', 'same-origin', 'include'];

  if (!isRSAA(action)) {
    validationErrors.push(
      'RSAAs must be plain JavaScript objects with an [RSAA] property'
    );
    return validationErrors;
  }

  const callAPI = action[RSAA];
  if (!isPlainObject(callAPI)) {
    validationErrors.push('[RSAA] property must be a plain JavaScript object');
  }
  for (let key in callAPI) {
    if (!~validCallAPIKeys.indexOf(key)) {
      validationErrors.push(`Invalid [RSAA] key: ${key}`);
    }
  }

  const {
    endpoint,
    method,
    headers,
    options,
    credentials,
    types,
    bailout,
    fetch,
    ok
  } = callAPI;
  if (typeof endpoint === 'undefined') {
    validationErrors.push('[RSAA] must have an endpoint property');
  } else if (typeof endpoint !== 'string' && typeof endpoint !== 'function') {
    validationErrors.push(
      '[RSAA].endpoint property must be a string or a function'
    );
  }
  if (typeof method === 'undefined') {
    validationErrors.push('[RSAA] must have a method property');
  } else if (typeof method !== 'string') {
    validationErrors.push('[RSAA].method property must be a string');
  } else if (!~validMethods.indexOf(method.toUpperCase())) {
    validationErrors.push(`Invalid [RSAA].method: ${method.toUpperCase()}`);
  }

  if (
    typeof headers !== 'undefined' &&
    !isPlainObject(headers) &&
    typeof headers !== 'function'
  ) {
    validationErrors.push(
      '[RSAA].headers property must be undefined, a plain JavaScript object, or a function'
    );
  }
  if (
    typeof options !== 'undefined' &&
    !isPlainObject(options) &&
    typeof options !== 'function'
  ) {
    validationErrors.push(
      '[RSAA].options property must be undefined, a plain JavaScript object, or a function'
    );
  }
  if (typeof credentials !== 'undefined') {
    if (typeof credentials !== 'string') {
      validationErrors.push(
        '[RSAA].credentials property must be undefined, or a string'
      );
    } else if (!~validCredentials.indexOf(credentials)) {
      validationErrors.push(`Invalid [RSAA].credentials: ${credentials}`);
    }
  }
  if (
    typeof bailout !== 'undefined' &&
    typeof bailout !== 'boolean' &&
    typeof bailout !== 'function'
  ) {
    validationErrors.push(
      '[RSAA].bailout property must be undefined, a boolean, or a function'
    );
  }

  if (typeof types === 'undefined') {
    validationErrors.push('[RSAA] must have a types property');
  } else if (!Array.isArray(types) || types.length !== 3) {
    validationErrors.push('[RSAA].types property must be an array of length 3');
  } else {
    const [requestType, successType, failureType] = types;
    if (
      typeof requestType !== 'string' &&
      typeof requestType !== 'symbol' &&
      !isValidTypeDescriptor(requestType)
    ) {
      validationErrors.push('Invalid request type');
    }
    if (
      typeof successType !== 'string' &&
      typeof successType !== 'symbol' &&
      !isValidTypeDescriptor(successType)
    ) {
      validationErrors.push('Invalid success type');
    }
    if (
      typeof failureType !== 'string' &&
      typeof failureType !== 'symbol' &&
      !isValidTypeDescriptor(failureType)
    ) {
      validationErrors.push('Invalid failure type');
    }
  }

  if (typeof fetch !== 'undefined') {
    if (typeof fetch !== 'function') {
      validationErrors.push('[RSAA].fetch property must be a function');
    }
  }

  if (typeof ok !== 'undefined') {
    if (typeof ok !== 'function') {
      validationErrors.push('[RSAA].ok property must be a function');
    }
  }

  return validationErrors;
}