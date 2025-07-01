function extractComments (contents) {
  let context = 'idle'
  const lines = []
  contents.split('\n').forEach((line) => {
    if (line.trim() === '/**') {
      context = 'in'
      return
    }

    if (line.trim() === '*/') {
      context = 'out'
      return
    }

    if (context === 'in') {
      lines.push(line.replace(/\*/g, '').replace(/^\s\s/, ''))
    }
  })
  return lines.join('\n')
}