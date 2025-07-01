public static void register(Binder binder, Class<?> clazz, Class<? extends Annotation> annotation)
  {
    registerKey(binder, Key.get(clazz, annotation));
  }