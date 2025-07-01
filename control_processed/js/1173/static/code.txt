function fileExistsWithCaseSync (filepath) {
  const { base, dir, root } = path.parse(filepath)

  if (dir === root || dir === '.') {
    return true
  }

  try {
    const filenames = fs.readdirSync(dir)
    if (!filenames.includes(base)) {
      return false
    }
  } catch (e) {
    // dir does not exist
    return false
  }

  return fileExistsWithCaseSync(dir)
}