protected static Type getTypeReference(Object type) {
        if (type instanceof Type) {
            return (Type) type;
        } else if (type instanceof Class) {
            return Type.getType((Class) type);
        } else if (type instanceof String) {
            String className = type.toString();

            String internalName = getInternalName(className);
            if (className.endsWith("[]")) {
                internalName = "[L" + internalName + ";";
            }
            return Type.getObjectType(internalName);
        } else {
            throw new IllegalArgumentException("Type reference [" + type + "] should be a Class or a String representing the class name");
        }
    }