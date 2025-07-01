public static Method getRequiredMethod(Class type, String name, Class... argumentTypes) {
        try {
            return type.getDeclaredMethod(name, argumentTypes);
        } catch (NoSuchMethodException e) {
            return findMethod(type, name, argumentTypes)
                .orElseThrow(() -> newNoSuchMethodError(type, name, argumentTypes));
        }
    }