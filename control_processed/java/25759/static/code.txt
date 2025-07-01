@Override public Chunk chunkForChunkIdx(int cidx) {
    Chunk crows = rows().chunkForChunkIdx(cidx);
    return new SubsetChunk(crows,this,masterVec());
  }