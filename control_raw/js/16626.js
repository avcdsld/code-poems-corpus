function execLinter(bin, args, execaOptions, pathsToLint) {
  const binArgs = args.concat(pathsToLint)

  debug('bin:', bin)
  debug('args: %O', binArgs)
  debug('opts: %o', execaOptions)

  return execa(bin, binArgs, { ...execaOptions })
}