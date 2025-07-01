public static Class<? extends Iced> getImplClass(Class<? extends Schema> clz) {
    Class<? extends Iced> impl_class = ReflectionUtils.findActualClassParameter(clz, 0);
    if (null == impl_class)
      Log.warn("Failed to find an impl class for Schema: " + clz);
    return impl_class;
  }