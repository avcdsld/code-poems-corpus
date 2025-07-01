@Override
  public void relocate(final int oldPosition, final int newPosition, final ByteBuffer oldBuf, final ByteBuffer newBuf)
  {
    HllSketch sketch = sketchCache.get(oldBuf).get(oldPosition);
    final WritableMemory oldMem = getMemory(oldBuf).writableRegion(oldPosition, size);
    if (sketch.isSameResource(oldMem)) { // sketch has not moved
      final WritableMemory newMem = getMemory(newBuf).writableRegion(newPosition, size);
      sketch = HllSketch.writableWrap(newMem);
    }
    putSketchIntoCache(newBuf, newPosition, sketch);
  }