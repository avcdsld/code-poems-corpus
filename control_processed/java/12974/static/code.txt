public static Method getSetter(String fieldName, Class<?> clazz, Class<?> fieldType) {
    String setterName = "set" + Character.toTitleCase(fieldName.charAt(0)) + fieldName.substring(1, fieldName.length());
    try {
      // Using getMethods(), getMethod(...) expects exact parameter type
      // matching and ignores inheritance-tree.
      Method[] methods = clazz.getMethods();
      for (Method method : methods) {
        if (method.getName().equals(setterName)) {
          Class<?>[] paramTypes = method.getParameterTypes();
          if (paramTypes != null && paramTypes.length == 1 && paramTypes[0].isAssignableFrom(fieldType)) {
            return method;
          }
        }
      }
      return null;
    } catch (SecurityException e) {
      throw new ActivitiException("Not allowed to access method " + setterName + " on class " + clazz.getCanonicalName());
    }
  }