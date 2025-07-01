function run(exec, args, shell, callback) {
    var env = extend({}, this.env)
    env.TERM = 'dumb'
    const opts = { env: env, shell: shell }

    this.log.silly('execFile: exec = %j', exec)
    this.log.silly('execFile: args = %j', args)
    this.log.silly('execFile: opts = %j', opts)
    try {
      this.execFile(exec, args, opts, execFileCallback.bind(this))
    } catch (err) {
      this.log.silly('execFile: threw:\n%s', err.stack)
      return callback(err)
    }

    function execFileCallback(err, stdout, stderr) {
      this.log.silly('execFile result: err = %j', err && err.stack || err)
      this.log.silly('execFile result: stdout = %j', stdout)
      this.log.silly('execFile result: stderr = %j', stderr)
      if (err) {
        return callback(err)
      }
      const execPath = stdout.trim()
      callback(null, execPath)
    }
  }