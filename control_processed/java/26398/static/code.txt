private static boolean sameType(Type[] types, Class<?>[] classes) {
        if (types.length != classes.length) return false;
        for (int i = 0; i < types.length; i++) {
            if (!Type.getType(classes[i]).equals(types[i])) return false;
        }
        return true;
    }