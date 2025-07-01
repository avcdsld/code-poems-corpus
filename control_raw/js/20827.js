function captureDoc(source, docStyleParsers, ...nodes) {
  const metadata = {}

  // 'some' short-circuits on first 'true'
  nodes.some(n => {
    try {

      let leadingComments

      // n.leadingComments is legacy `attachComments` behavior
      if ('leadingComments' in n) {
        leadingComments = n.leadingComments
      } else if (n.range) {
        leadingComments = source.getCommentsBefore(n)
      }

      if (!leadingComments || leadingComments.length === 0) return false

      for (let name in docStyleParsers) {
        const doc = docStyleParsers[name](leadingComments)
        if (doc) {
          metadata.doc = doc
        }
      }

      return true
    } catch (err) {
      return false
    }
  })

  return metadata
}