public SharedTreeSubgraph getSharedTreeSubgraph(final int tidx, final int cls) {
    if (tidx < 0 || tidx >= _output._ntrees) {
      throw new IllegalArgumentException("Invalid tree index: " + tidx +
              ". Tree index must be in range [0, " + (_output._ntrees -1) + "].");
    }
    final CompressedTree auxCompressedTree = _output._treeKeysAux[tidx][cls].get();
    return _output._treeKeys[tidx][cls].get().toSharedTreeSubgraph(auxCompressedTree, _output._names, _output._domains);
  }