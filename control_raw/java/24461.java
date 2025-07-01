public boolean closeClassLoader(final ClassLoader cl) throws ValidatorManagerException {
    boolean res = false;
    if (cl == null) {
      return res;
    }
    final Class classURLClassLoader = URLClassLoader.class;
    Field f = null;
    try {
      f = classURLClassLoader.getDeclaredField("ucp");
    } catch (final NoSuchFieldException e) {
      throw new ValidatorManagerException(e);
    }
    if (f != null) {
      f.setAccessible(true);
      Object obj = null;
      try {
        obj = f.get(cl);
      } catch (final IllegalAccessException e) {
        throw new ValidatorManagerException(e);
      }
      if (obj != null) {
        final Object ucp = obj;
        f = null;
        try {
          f = ucp.getClass().getDeclaredField("loaders");
        } catch (final NoSuchFieldException e) {
          throw new ValidatorManagerException(e);
        }
        if (f != null) {
          f.setAccessible(true);
          ArrayList loaders = null;
          try {
            loaders = (ArrayList) f.get(ucp);
            res = true;
          } catch (final IllegalAccessException e) {
            throw new ValidatorManagerException(e);
          }
          for (int i = 0; loaders != null && i < loaders.size(); i++) {
            obj = loaders.get(i);
            f = null;
            try {
              f = obj.getClass().getDeclaredField("jar");
            } catch (final NoSuchFieldException e) {
              throw new ValidatorManagerException(e);
            }
            if (f != null) {
              f.setAccessible(true);
              try {
                obj = f.get(obj);
              } catch (final IllegalAccessException e) {
                throw new ValidatorManagerException(e);
              }
              if (obj instanceof JarFile) {
                final JarFile jarFile = (JarFile) obj;
                this.setJarFileNames2Close.add(jarFile.getName());
                try {
                  jarFile.close();
                } catch (final IOException e) {
                  throw new ValidatorManagerException(e);
                }
              }
            }
          }
        }
      }
    }
    return res;
  }