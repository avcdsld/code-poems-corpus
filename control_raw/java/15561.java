private static String computeKeyHash(String memcachedPrefix, NamedKey key)
  {
    // hash keys to keep things under 250 characters for memcached
    return memcachedPrefix + ":" + DigestUtils.sha1Hex(key.namespace) + ":" + DigestUtils.sha1Hex(key.key);
  }