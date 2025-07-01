public static Method getMethod(String clazzName, String methodName, String[] argsType) {
        Class clazz = ClassUtils.forName(clazzName);
        Class[] classes = ClassTypeUtils.getClasses(argsType);
        return getMethod(clazz, methodName, classes);
    }