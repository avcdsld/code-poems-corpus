function NetProfiler (options = {}) {
  if (!(this instanceof NetProfiler)) return new NetProfiler(options)

  if (!options.net) {
    options.net = require('net')
  }

  this.net = options.net
  this.proxies = {}
  this.activeConnections = []
  this.startTs = new Date() / 1000
  this.tickMs = options.tickMs || 1000
  this.tickWhenNoneActive = options.tickWhenNoneActive || false

  this.logPath = getLogPath(options.logPath)
  debug('logging to ', this.logPath)

  this.startProfiling()
}