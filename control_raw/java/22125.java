protected Map<String, Object> resolveGenericTypes(TypeMirror type, Map<String, Object> boundTypes) {
        if (type.getKind().isPrimitive() || type.getKind() == VOID || type.getKind() == ARRAY) {
            return Collections.emptyMap();
        }
        if (type instanceof DeclaredType) {
            DeclaredType declaredType = (DeclaredType) type;
            return resolveGenericTypes(declaredType, (TypeElement) declaredType.asElement(), boundTypes);
        } else if (type instanceof TypeVariable) {
            TypeVariable var = (TypeVariable) type;
            TypeMirror upperBound = var.getUpperBound();
            if (upperBound instanceof DeclaredType) {
                return resolveGenericTypes(upperBound, boundTypes);
            }
        }
        return Collections.emptyMap();
    }