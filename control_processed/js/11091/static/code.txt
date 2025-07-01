function isFunction(value) {
      if (!isObject(value)) {
        return false;
      }//--•

      // The use of `Object#toString` avoids issues with the `typeof` operator
      // in older versions of Chrome and Safari which return 'function' for regexes
      // and Safari 8 which returns 'object' for typed array constructors.
      var tag = objToString.call(value);

      // Return true if this looks like a function, an "async function", a "generator", or a "proxy".
      return tag == funcTag || tag == genTag || tag == asyncTag || tag == proxyTag;

      // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      // ^^^^
      // PATCHED FROM https://github.com/lodash/lodash/commit/95bc54a3ddc7a25f5e134f5b376a0d1d96118f49
      // Note that, in Lodash 4, this looks like:
      // ```
      // return tag == funcTag || tag == genTag || tag == asyncTag || tag == proxyTag;
      // ```
      // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    }