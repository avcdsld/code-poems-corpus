function isNativeFunction(f) {
	  var reRegExpChar = /[\\^$.*+?()[\]{}|]/g;
	  var funcMatchString = Function.prototype.toString.call(Object.prototype.hasOwnProperty)
	    .replace(reRegExpChar, '\\$&')
	    .replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g, '$1.*?');
	  var reIsNative = RegExp('^' + funcMatchString + '$');
	  return isObject(f) && reIsNative.test(f);
	}