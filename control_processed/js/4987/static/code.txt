function mergeEdges(
  sourceEdges: Array<?RecordProxy>,
  targetEdges: Array<?RecordProxy>,
  nodeIDs: Set<mixed>,
): void {
  const {NODE} = RelayConnectionInterface.get();

  for (let ii = 0; ii < sourceEdges.length; ii++) {
    const edge = sourceEdges[ii];
    if (!edge) {
      continue;
    }
    const node = edge.getLinkedRecord(NODE);
    const nodeID = node && node.getValue('id');
    if (nodeID) {
      if (nodeIDs.has(nodeID)) {
        continue;
      }
      nodeIDs.add(nodeID);
    }
    targetEdges.push(edge);
  }
}