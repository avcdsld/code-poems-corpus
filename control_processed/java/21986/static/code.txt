protected <T> TypeConverter findTypeConverter(Class<?> sourceType, Class<T> targetType, Class<? extends Annotation> formattingAnnotation) {
        TypeConverter typeConverter = null;
        List<Class> sourceHierarchy = ClassUtils.resolveHierarchy(sourceType);
        List<Class> targetHierarchy = ClassUtils.resolveHierarchy(targetType);
        boolean hasFormatting = formattingAnnotation != null;
        for (Class sourceSuperType : sourceHierarchy) {
            for (Class targetSuperType : targetHierarchy) {
                ConvertiblePair pair = new ConvertiblePair(sourceSuperType, targetSuperType, formattingAnnotation);
                typeConverter = typeConverters.get(pair);
                if (typeConverter != null) {
                    converterCache.put(pair, typeConverter);
                    return typeConverter;
                }
            }
        }
        if (hasFormatting) {
            for (Class sourceSuperType : sourceHierarchy) {
                for (Class targetSuperType : targetHierarchy) {
                    ConvertiblePair pair = new ConvertiblePair(sourceSuperType, targetSuperType);
                    typeConverter = typeConverters.get(pair);
                    if (typeConverter != null) {
                        converterCache.put(pair, typeConverter);
                        return typeConverter;
                    }
                }
            }
        }
        return typeConverter;
    }