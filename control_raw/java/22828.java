static Map<Method, Setter> toSetters(SetterFactory setterFactory,
                                       Target<?> target,
                                       Set<Method> methods) {
    Map<Method, Setter> result = new LinkedHashMap<Method, Setter>();
    for (Method method : methods) {
      method.setAccessible(true);
      result.put(method, setterFactory.create(target, method));
    }
    return result;
  }