function (directory) {
  try {
    const content = fs.readFileSync(path.join(directory, CONFIG_EXAMPLE_FILE), 'utf8')
    if (process.env.VERBOSE) {
      console.log('You need to configure the connector in your deepstream configuration file')
    }
    if (!process.env.QUIET) {
      console.log(`Example configuration:\n${colors.grey(content)}`)
    }
  } catch (err) {
    if (!process.env.QUIET) {
      console.log('Example configuration not found')
    }
  }
}