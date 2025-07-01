protected static String getTypeDescriptor(Object type) {
        if (type instanceof Class) {
            return Type.getDescriptor((Class) type);
        } else if (type instanceof Type) {
            return ((Type) type).getDescriptor();
        } else {
            String className = type.toString();
            return getTypeDescriptor(className, new String[0]);
        }
    }