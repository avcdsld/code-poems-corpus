public boolean finalizeNativeLibs(final ClassLoader cl) throws ValidatorManagerException {
    boolean res = false;
    final Class classClassLoader = ClassLoader.class;
    java.lang.reflect.Field nativeLibraries = null;
    try {
      nativeLibraries = classClassLoader.getDeclaredField("nativeLibraries");
    } catch (final NoSuchFieldException e) {
      throw new ValidatorManagerException(e);
    }
    if (nativeLibraries == null) {
      return res;
    }
    nativeLibraries.setAccessible(true);
    Object obj = null;
    try {
      obj = nativeLibraries.get(cl);
    } catch (final IllegalAccessException e) {
      throw new ValidatorManagerException(e);
    }
    if (!(obj instanceof Vector)) {
      return res;
    }
    res = true;
    final Vector java_lang_ClassLoader_NativeLibrary = (Vector) obj;
    for (final Object lib : java_lang_ClassLoader_NativeLibrary) {
      java.lang.reflect.Method finalize = null;
      try {
        finalize = lib.getClass().getDeclaredMethod("finalize", new Class[0]);
      } catch (final NoSuchMethodException e) {
        throw new ValidatorManagerException(e);
      }
      if (finalize != null) {
        finalize.setAccessible(true);
        try {
          finalize.invoke(lib, new Object[0]);
        } catch (final IllegalAccessException e) {
          throw new ValidatorManagerException(e);
        } catch (final InvocationTargetException e) {
          throw new ValidatorManagerException(e);
        }
      }
    }
    return res;
  }