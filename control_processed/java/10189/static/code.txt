private static String inet6AddressToAscii(byte[] address) {
    // Go through the address looking for the longest run of 0s. Each group is 2-bytes.
    // A run must be longer than one group (section 4.2.2).
    // If there are multiple equal runs, the first one must be used (section 4.2.3).
    int longestRunOffset = -1;
    int longestRunLength = 0;
    for (int i = 0; i < address.length; i += 2) {
      int currentRunOffset = i;
      while (i < 16 && address[i] == 0 && address[i + 1] == 0) {
        i += 2;
      }
      int currentRunLength = i - currentRunOffset;
      if (currentRunLength > longestRunLength && currentRunLength >= 4) {
        longestRunOffset = currentRunOffset;
        longestRunLength = currentRunLength;
      }
    }

    // Emit each 2-byte group in hex, separated by ':'. The longest run of zeroes is "::".
    Buffer result = new Buffer();
    for (int i = 0; i < address.length; ) {
      if (i == longestRunOffset) {
        result.writeByte(':');
        i += longestRunLength;
        if (i == 16) result.writeByte(':');
      } else {
        if (i > 0) result.writeByte(':');
        int group = (address[i] & 0xff) << 8 | address[i + 1] & 0xff;
        result.writeHexadecimalUnsignedLong(group);
        i += 2;
      }
    }
    return result.readUtf8();
  }