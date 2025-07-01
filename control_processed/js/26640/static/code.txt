function each (obj, iterate, context) {
  if (obj) {
    context = context || this
    if (isArray(obj)) {
      return arrayEach(obj, iterate, context)
    }
    return objectEach(obj, iterate, context)
  }
  return obj
}