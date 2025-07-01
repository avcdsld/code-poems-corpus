function replaceInFile (filename, regex, replacement) {
    log.bright.cyan ('Exporting exchanges →', filename.yellow)
    let contents = fs.readFileSync (filename, 'utf8')
    const newContents = contents.replace (regex, replacement)
    fs.truncateSync (filename)
    fs.writeFileSync (filename, newContents)
}