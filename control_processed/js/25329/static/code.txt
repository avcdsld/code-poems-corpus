function get(obj, path) {
	  if (!obj) {
	    return undefined;
	  }
	  var keys = path.split('.');
	  var result = obj;
	  try {
	    for (var i = 0, len = keys.length; i < len; ++i) {
	      result = result[keys[i]];
	    }
	  } catch (e) {
	    result = undefined;
	  }
	  return result;
	}