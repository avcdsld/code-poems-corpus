public byte[] getKey() {
    if (result == null) {
      return null;
    }
    if (result.getKeyData().size() < KEY_LENGTH) {
      throw new IllegalStateException("Could not get enough key data from the handshake.");
    }
    byte[] key = new byte[KEY_LENGTH];
    result.getKeyData().copyTo(key, 0, 0, KEY_LENGTH);
    return key;
  }