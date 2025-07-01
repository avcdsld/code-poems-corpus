function formatValues(values) {
  var formatted = {};
  for (var key in values) {
    if (values.hasOwnProperty(key)) {
      if (typeof values[key] === 'boolean') {
        var position = key.indexOf('{');
        if (position !== -1) {
          if (values[key] === true) {
            // Each options of SelectWidget are stored as boolean and grouped using '{' and '}'
            // eg:
            // gender{male} = true
            // gender{female} = false
            var newKey = key.substr(0, position);
            var newValue = key.substr(position);
            newValue = newValue.replace('{', '');
            newValue = newValue.replace('}', '');
            if (!Array.isArray(formatted[newKey])) {
              formatted[newKey] = [];
            }
            formatted[newKey].push(newValue);
          }
        } else {
          formatted[key] = values[key];
        }
      } else {
        if (typeof values[key] === 'string') {
          formatted[key] = values[key].trim();
        } else {
          formatted[key] = values[key];
        }
      }
    }
  }
  return formatted;
}