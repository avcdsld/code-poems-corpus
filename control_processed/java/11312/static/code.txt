private ResourceBundleHolder loadMessageBundle(Method m) throws ClassNotFoundException {
        Class c = m.getDeclaringClass();
        Class<?> msg = c.getClassLoader().loadClass(c.getName().substring(0, c.getName().lastIndexOf(".")) + ".Messages");
        return ResourceBundleHolder.get(msg);
    }