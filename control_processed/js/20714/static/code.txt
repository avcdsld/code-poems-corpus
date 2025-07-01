function(content, depth = 0, options = {}) {
    var i, indent, isBoolean, isNull, isObj, j, k, out, prefix, ref, v;
    if (arguments.length === 2) {
      options = depth;
      depth = 0;
    }
    if (options.separator == null) {
      options.separator = ' = ';
    }
    if (options.eol == null) {
      options.eol = !options.ssh && process.platform === "win32" ? "\r\n" : "\n";
    }
    out = '';
    indent = options.indent != null ? options.indent : '  ';
    prefix = '';
    for (i = j = 0, ref = depth; (0 <= ref ? j < ref : j > ref); i = 0 <= ref ? ++j : --j) {
      prefix += indent;
    }
    for (k in content) {
      v = content[k];
      // isUndefined = typeof v is 'undefined'
      isBoolean = typeof v === 'boolean';
      isNull = v === null;
      isObj = typeof v === 'object' && !isNull;
      if (isObj) {
        continue;
      }
      if (isNull) {
        out += `${prefix}${k}`;
      } else if (isBoolean) {
        out += `${prefix}${k}${options.separator}${(v ? 'true' : 'false')}`;
      } else {
        out += `${prefix}${k}${options.separator}${v}`;
      }
      out += `${options.eol}`;
    }
    for (k in content) {
      v = content[k];
      isNull = v === null;
      isObj = typeof v === 'object' && !isNull;
      if (!isObj) {
        continue;
      }
      out += `${prefix}${string.repeat('[', depth + 1)}${k}${string.repeat(']', depth + 1)}${options.eol}`;
      out += module.exports.stringify_multi_brackets(v, depth + 1, options);
    }
    return out;
  }