function truncate (element, options) {
  const truncator = new Truncator(element, options)
  if (truncator) {
    return truncator.truncate()
  }
}