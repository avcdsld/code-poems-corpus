function ensureBoolean(value) {
  if (typeof value === 'boolean') {
    return value;
  }
  if (typeof value === 'string' && value.toLowerCase() === 'true') {
    return true;
  } else if (typeof value === 'string' && value.toLowerCase() === 'false') {
    return false;
  } else if (value === 1) {
    return true;
  } else if (value === 0) {
    return false;
  }
  throw new Error(`Unexpected value for boolean: ${value}`);
}