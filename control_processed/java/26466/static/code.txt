private void invoke(WebSocketContext ctx, Class<? extends Annotation> event) {
        Map<Class<? extends Annotation>, Method> methodCache = this.methodCache.get(path.get());
        if (methodCache != null) {
            Method method = methodCache.get(event);
            if (method != null) {
                Class<?>[] paramTypes = method.getParameterTypes();
                Object[] param = new Object[paramTypes.length];
                try {
                    for (int i = 0; i < paramTypes.length; i++) {
                        Class<?> paramType = paramTypes[i];
                        if (paramType == WebSocketContext.class) {
                            param[i] = ctx;
                        } else {
                            Object bean = this.blade.getBean(paramType);
                            if (bean != null) {
                                param[i] = bean;
                            } else {
                                param[i] = ReflectKit.newInstance(paramType);
                            }
                        }
                    }
                    method.invoke(blade.getBean(handlers.get(path.get())), param);
                } catch (IllegalAccessException | InvocationTargetException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }