function collapse(edgeIndex, nodeMap, remainingEdges) {
  if (remainingEdges.length === 0) {
    error("Karger-Stein must be run on a connected (sub)graph");
  }

  var edgeInfo = remainingEdges[edgeIndex];
  var sourceIn = edgeInfo[1];
  var targetIn = edgeInfo[2];
  var partition1 = nodeMap[sourceIn];
  var partition2 = nodeMap[targetIn];
  var newEdges = remainingEdges; // re-use array
  // Delete all edges between partition1 and partition2

  for (var i = newEdges.length - 1; i >= 0; i--) {
    var edge = newEdges[i];
    var src = edge[1];
    var tgt = edge[2];

    if (nodeMap[src] === partition1 && nodeMap[tgt] === partition2 || nodeMap[src] === partition2 && nodeMap[tgt] === partition1) {
      newEdges.splice(i, 1);
    }
  } // All edges pointing to partition2 should now point to partition1


  for (var _i = 0; _i < newEdges.length; _i++) {
    var _edge = newEdges[_i];

    if (_edge[1] === partition2) {
      // Check source
      newEdges[_i] = _edge.slice(); // copy

      newEdges[_i][1] = partition1;
    } else if (_edge[2] === partition2) {
      // Check target
      newEdges[_i] = _edge.slice(); // copy

      newEdges[_i][2] = partition1;
    }
  } // Move all nodes from partition2 to partition1


  for (var _i2 = 0; _i2 < nodeMap.length; _i2++) {
    if (nodeMap[_i2] === partition2) {
      nodeMap[_i2] = partition1;
    }
  }

  return newEdges;
}