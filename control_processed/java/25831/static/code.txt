public SharedTreeNode makeRootNode() {
    assert nodesArray.size() == 0;
    SharedTreeNode n = new SharedTreeNode(0, null, subgraphNumber, 0);
    n.setInclusiveNa(true);
    nodesArray.add(n);
    rootNode = n;
    return n;
  }