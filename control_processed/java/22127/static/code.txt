protected Object resolveTypeReference(TypeMirror mirror, Map<String, Object> boundTypes) {
        TypeKind kind = mirror.getKind();
        switch (kind) {
            case TYPEVAR:
                TypeVariable tv = (TypeVariable) mirror;
                String name = tv.toString();
                if (boundTypes.containsKey(name)) {
                    return boundTypes.get(name);
                } else {
                    return modelUtils.resolveTypeReference(mirror);
                }
            case WILDCARD:
                WildcardType wcType = (WildcardType) mirror;
                TypeMirror extendsBound = wcType.getExtendsBound();
                TypeMirror superBound = wcType.getSuperBound();
                if (extendsBound == null && superBound == null) {
                    return Object.class.getName();
                } else if (extendsBound != null) {
                    return resolveTypeReference(typeUtils.erasure(extendsBound), boundTypes);
                } else if (superBound != null) {
                    return resolveTypeReference(superBound, boundTypes);
                } else {
                    return resolveTypeReference(typeUtils.getWildcardType(extendsBound, superBound), boundTypes);
                }
            case ARRAY:
                ArrayType arrayType = (ArrayType) mirror;
                Object reference = resolveTypeReference(arrayType.getComponentType(), boundTypes);
                if (reference instanceof Class) {
                    Class componentType = (Class) reference;
                    return Array.newInstance(componentType, 0).getClass();
                } else if (reference instanceof String) {
                    return reference + "[]";
                } else {
                    return modelUtils.resolveTypeReference(mirror);
                }
            case BOOLEAN:
            case BYTE:
            case CHAR:
            case DOUBLE:
            case FLOAT:
            case INT:
            case LONG:
            case SHORT:
                Optional<Class> type = ClassUtils.getPrimitiveType(mirror.toString());
                if (type.isPresent()) {
                    return type.get();
                } else {
                    throw new IllegalStateException("Unknown primitive type: " + mirror.toString());
                }
            default:
                return modelUtils.resolveTypeReference(mirror);
        }
    }