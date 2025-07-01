public void writeAscii(long v) {
    if (v == 0) {
      writeByte('0');
      return;
    }

    if (v == Long.MIN_VALUE) {
      writeAscii("-9223372036854775808");
      return;
    }

    if (v < 0) {
      writeByte('-');
      v = -v; // needs to be positive so we can use this for an array index
    }

    writeBackwards(v);
  }