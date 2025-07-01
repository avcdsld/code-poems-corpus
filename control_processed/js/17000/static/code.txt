function resetState () {
  index = queue.length = 0
  has = {}
  /* istanbul ignore if */
  if (process.env.NODE_ENV !== 'production') {
    circular = {}
  }
  flushing = false
}