public static Class[] resolveInterfaceTypeArguments(Class<?> type, Class<?> interfaceType) {
        Optional<Type> resolvedType = getAllGenericInterfaces(type)
                .stream()
                .filter(t -> {
                            if (t instanceof ParameterizedType) {
                                ParameterizedType pt = (ParameterizedType) t;
                                return pt.getRawType() == interfaceType;
                            }
                            return false;
                        }
                )
                .findFirst();
        return resolvedType.map(GenericTypeUtils::resolveTypeArguments)
                .orElse(ReflectionUtils.EMPTY_CLASS_ARRAY);
    }