public static long objectFieldOffset(Class<?> clazz, String fieldName) {
    try {
      return UNSAFE.objectFieldOffset(clazz.getDeclaredField(fieldName));
    } catch (NoSuchFieldException | SecurityException e) {
      throw new Error(e);
    }
  }