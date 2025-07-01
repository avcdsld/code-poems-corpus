function recordTiming (name, timing) {
  recorder[name] = parseInt(timing, 10) || Date.now()
  performanceEvent.trigger('update', getTiming())
}