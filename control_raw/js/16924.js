function start (startTiming) {
  if (isStart) {
    return
  }
  isStart = true
  recordTiming('MIPStart', startTiming)
  viewer.on('show', showTiming => {
    recordTiming('MIPPageShow', showTiming)
  })

  document.addEventListener('DOMContentLoaded', domLoaded, false)
  document.onreadystatechange = () => {
    if (document.readyState === 'complete') {
      domLoaded()
    }
  }
}