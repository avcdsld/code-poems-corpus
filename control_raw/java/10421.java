private Object execute(Object o, Method m, Object... args) throws CommandActionExecutionException {
        Object result = null;
        try {
            m.setAccessible(true); // suppress Java language access
            if (isCompileWeaving() && metaHolder.getAjcMethod() != null) {
                result = invokeAjcMethod(metaHolder.getAjcMethod(), o, metaHolder, args);
            } else {
                result = m.invoke(o, args);
            }
        } catch (IllegalAccessException e) {
            propagateCause(e);
        } catch (InvocationTargetException e) {
            propagateCause(e);
        }
        return result;
    }