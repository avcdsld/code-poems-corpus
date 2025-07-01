private void flush(FlushType flushType) throws IOException {
    switch (flushType) {
      case WRAP:
        out.append('\n');
        for (int i = 0; i < indentLevel; i++) {
          out.append(indent);
        }
        column = indentLevel * indent.length();
        column += buffer.length();
        break;
      case SPACE:
        out.append(' ');
        break;
      case EMPTY:
        break;
      default:
        throw new IllegalArgumentException("Unknown FlushType: " + flushType);
    }

    out.append(buffer);
    buffer.delete(0, buffer.length());
    indentLevel = -1;
    nextFlush = null;
  }