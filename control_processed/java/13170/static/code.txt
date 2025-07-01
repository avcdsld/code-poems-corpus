static byte[] writeTraces(SpanBytesEncoder codec, List<List<zipkin2.Span>> traces) {
    // Get the encoded size of the nested list so that we don't need to grow the buffer
    int length = traces.size();
    int sizeInBytes = 2; // []
    if (length > 1) sizeInBytes += length - 1; // comma to join elements

    for (int i = 0; i < length; i++) {
      List<zipkin2.Span> spans = traces.get(i);
      int jLength = spans.size();
      sizeInBytes += 2; // []
      if (jLength > 1) sizeInBytes += jLength - 1; // comma to join elements
      for (int j = 0; j < jLength; j++) {
        sizeInBytes += codec.sizeInBytes(spans.get(j));
      }
    }

    byte[] out = new byte[sizeInBytes];
    int pos = 0;
    out[pos++] = '['; // start list of traces
    for (int i = 0; i < length; i++) {
      pos += codec.encodeList(traces.get(i), out, pos);
      if (i + 1 < length) out[pos++] = ',';
    }
    out[pos] = ']'; // stop list of traces
    return out;
  }