function doBuild () {
    // Enable Verbose build
    var verbose = log.levels[log.level] <= log.levels.verbose
    if (!win && verbose) {
      argv.push('V=1')
    }
    if (win && !verbose) {
      argv.push('/clp:Verbosity=minimal')
    }

    if (win) {
      // Turn off the Microsoft logo on Windows
      argv.push('/nologo')
    }

    // Specify the build type, Release by default
    if (win) {
      // Convert .gypi config target_arch to MSBuild /Platform
      // Since there are many ways to state '32-bit Intel', default to it.
      // N.B. msbuild's Condition string equality tests are case-insensitive.
      var archLower = arch.toLowerCase()
      var p = archLower === 'x64' ? 'x64' :
              (archLower === 'arm' ? 'ARM' :
              (archLower === 'arm64' ? 'ARM64' : 'Win32'))
      argv.push('/p:Configuration=' + buildType + ';Platform=' + p)
      if (jobs) {
        var j = parseInt(jobs, 10)
        if (!isNaN(j) && j > 0) {
          argv.push('/m:' + j)
        } else if (jobs.toUpperCase() === 'MAX') {
          argv.push('/m:' + require('os').cpus().length)
        }
      }
    } else {
      argv.push('BUILDTYPE=' + buildType)
      // Invoke the Makefile in the 'build' dir.
      argv.push('-C')
      argv.push('build')
      if (jobs) {
        var j = parseInt(jobs, 10)
        if (!isNaN(j) && j > 0) {
          argv.push('--jobs')
          argv.push(j)
        } else if (jobs.toUpperCase() === 'MAX') {
          argv.push('--jobs')
          argv.push(require('os').cpus().length)
        }
      }
    }

    if (win) {
      // did the user specify their own .sln file?
      var hasSln = argv.some(function (arg) {
        return path.extname(arg) == '.sln'
      })
      if (!hasSln) {
        argv.unshift(gyp.opts.solution || guessedSolution)
      }
    }

    var proc = gyp.spawn(command, argv)
    proc.on('exit', onExit)
  }