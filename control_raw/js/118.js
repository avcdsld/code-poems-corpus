function sortTopologically (originalOrder, edgesById) {
  const sorted = []
  const marked = new Set()

  const visit = (mark) => {
    if (marked.has(mark)) return
    marked.add(mark)
    const edges = edgesById.get(mark)
    if (edges != null) {
      edges.forEach(visit)
    }
    sorted.push(mark)
  }

  originalOrder.forEach(visit)
  return sorted
}