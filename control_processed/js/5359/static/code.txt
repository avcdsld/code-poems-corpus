function normalizeRowColumn (str) {
  let normalized = parser(str)
    .nodes
    .reduce((result, node) => {
      if (node.type === 'function' && node.value === 'repeat') {
        let key = 'count'

        let [count, value] = node.nodes.reduce((acc, n) => {
          if (n.type === 'word' && key === 'count') {
            acc[0] = Math.abs(parseInt(n.value))
            return acc
          }
          if (n.type === 'div' && n.value === ',') {
            key = 'value'
            return acc
          }
          if (key === 'value') {
            acc[1] += parser.stringify(n)
          }
          return acc
        }, [0, ''])

        if (count) {
          for (let i = 0; i < count; i++) {
            result.push(value)
          }
        }

        return result
      }
      if (node.type === 'space') {
        return result
      }
      return result.concat(parser.stringify(node))
    }, [])

  return normalized
}