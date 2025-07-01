private StreamInfo readOneFile(final InputStream is, final StreamParseWriter dout, InputStream bvs,
                                 StreamParseWriter nextChunk, int zidx, int fileIndex) throws IOException {
    int cidx = 0;
    StreamData din = new StreamData(is);
    // only check header for 2nd file onward since guess setup is already done on first file.
    if ((fileIndex > 0) && (!checkFileNHeader(is, dout, din, cidx))) // cidx should be the actual column index
      return new StreamInfo(zidx, nextChunk);  // header is bad, quit now
    int streamAvailable = is.available();
    while (streamAvailable > 0) {
      parseChunk(cidx++, din, nextChunk); // cidx here actually goes and get the right column chunk.
      streamAvailable = is.available(); // Can (also!) rollover to the next input chunk
      int xidx = bvs.read(null, 0, 0); // Back-channel read of chunk index
      if (xidx > zidx) {  // Advanced chunk index of underlying ByteVec stream?
        zidx = xidx;       // Record advancing of chunk
        nextChunk.close(); // Match output chunks to input zipfile chunks
        if (dout != nextChunk) {
          dout.reduce(nextChunk);
          if (_jobKey != null && _jobKey.get().stop_requested()) break;
        }
        nextChunk = nextChunk.nextChunk();
      }
    }
    parseChunk(cidx, din, nextChunk);
    return new StreamInfo(zidx, nextChunk);
  }