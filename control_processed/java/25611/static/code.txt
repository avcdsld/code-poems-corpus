public static <T extends Schema>  void setField(T o, Field f, String key, String value, boolean required, Class thisSchemaClass) throws IllegalAccessException {
    // Primitive parse by field type
    Object parse_result = parse(key, value, f.getType(), required, thisSchemaClass);
    if (parse_result != null && f.getType().isArray() && parse_result.getClass().isArray() && (f.getType().getComponentType() != parse_result.getClass().getComponentType())) {
      // We have to conform an array of primitives.  There's got to be a better way. . .
      if (parse_result.getClass().getComponentType() == int.class && f.getType().getComponentType() == Integer.class) {
        int[] from = (int[])parse_result;
        Integer[] copy = new Integer[from.length];
        for (int i = 0; i < from.length; i++)
          copy[i] = from[i];
        f.set(o, copy);
      } else if (parse_result.getClass().getComponentType() == Integer.class && f.getType().getComponentType() == int.class) {
        Integer[] from = (Integer[])parse_result;
        int[] copy = new int[from.length];
        for (int i = 0; i < from.length; i++)
          copy[i] = from[i];
        f.set(o, copy);
      } else if (parse_result.getClass().getComponentType() == Double.class && f.getType().getComponentType() == double.class) {
        Double[] from = (Double[])parse_result;
        double[] copy = new double[from.length];
        for (int i = 0; i < from.length; i++)
          copy[i] = from[i];
        f.set(o, copy);
      } else if (parse_result.getClass().getComponentType() == Float.class && f.getType().getComponentType() == float.class) {
        Float[] from = (Float[])parse_result;
        float[] copy = new float[from.length];
        for (int i = 0; i < from.length; i++)
          copy[i] = from[i];
        f.set(o, copy);
      } else {
        throw H2O.fail("Don't know how to cast an array of: " + parse_result.getClass().getComponentType() + " to an array of: " + f.getType().getComponentType());
      }
    } else {
      f.set(o, parse_result);
    }
  }