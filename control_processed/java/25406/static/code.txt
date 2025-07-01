private static String credentialMD5digest(String password) {
    try {
      byte[] digest;
      synchronized (__md5Lock) {
        if (__md == null) {
          try {
            __md = MessageDigest.getInstance("MD5");
          } catch (Exception e) {
            throw new IllegalStateException(e);
          }
        }

        __md.reset();
        __md.update(password.getBytes(StandardCharsets.ISO_8859_1));
        digest = __md.digest();
      }

      return __TYPE + toString(digest, 16);
    } catch (Exception e) {
      throw new IllegalStateException(e);
    }
  }