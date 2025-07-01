private Method findResolver(Class type) throws IOException {
        List<Method> resolvers = Util.filter(Index.list(CLIResolver.class, Jenkins.get().getPluginManager().uberClassLoader), Method.class);
        for ( ; type!=null; type=type.getSuperclass())
            for (Method m : resolvers)
                if (m.getReturnType()==type)
                    return m;
        return null;
    }