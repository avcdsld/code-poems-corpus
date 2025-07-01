function readJson(filePath) {
  try {
    const content = readFile(filePath)
    return JSON.parse(content)
  } catch (err) {
    return null
  }
}