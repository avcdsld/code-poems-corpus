function internalStringify(holder, key) {
    var buffer, res;

    // Replace the value, if necessary
    var obj_part = getReplacedValueOrUndefined(holder, key);

    if (obj_part && !isDate(obj_part)) {
      // unbox objects
      // don't unbox dates, since will turn it into number
      obj_part = obj_part.valueOf();
    }
    switch (typeof obj_part) {
      case 'boolean':
        return obj_part.toString();

      case 'number':
        if (isNaN(obj_part) || !isFinite(obj_part)) {
          return 'null';
        }
        return obj_part.toString();

      case 'string':
        return escapeString(obj_part.toString());

      case 'object':
        if (obj_part === null) {
          return 'null';
        } else if (isArray(obj_part)) {
          checkForCircular(obj_part);
          buffer = '[';
          objStack.push(obj_part);

          for (var i = 0; i < obj_part.length; i++) {
            res = internalStringify(obj_part, i);
            if (res === null) {
              buffer += 'null';
            } /* else if (typeof res === 'undefined') {  // modified to support empty array values
              buffer += '';
            }*/ else {
              buffer += res;
            }
            if (i < obj_part.length - 1) {
              buffer += ',';
            }
          }
          objStack.pop();
          buffer += ']';
        } else {
          checkForCircular(obj_part);
          buffer = '{';
          var nonEmpty = false;
          objStack.push(obj_part);
          for (var prop in obj_part) {
            if (obj_part.hasOwnProperty(prop)) {
              var value = internalStringify(obj_part, prop);
              if (typeof value !== 'undefined' && value !== null) {
                nonEmpty = true;
                key = isWord(prop) && !quoteKeys ? prop : escapeString(prop, quoteKeys);
                buffer += key + ':' + value + ',';
              }
            }
          }
          objStack.pop();
          if (nonEmpty) {
            buffer = buffer.substring(0, buffer.length - 1) + '}';
          } else {
            buffer = '{}';
          }
        }
        return buffer;
      default:
        // functions and undefined should be ignored
        return undefined;
    }
  }