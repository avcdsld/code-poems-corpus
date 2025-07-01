function forEachObject(object, callback, context) {
  for (var name in object) {
    if (hasOwnProperty.call(object, name)) {
      callback.call(context, object[name], name, object);
    }
  }
}