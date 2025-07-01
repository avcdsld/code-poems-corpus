private static int typeCode(Object a) {
        if (a instanceof java.lang.Integer) return INT;
        if (a instanceof java.lang.Double) return DOUBLE;
        if (a instanceof java.lang.Long) return LONG;
        if (a instanceof java.lang.Character) return CHAR;
        if (a instanceof java.lang.Float) return FLOAT;
        if ((a instanceof java.lang.Byte) || (a instanceof java.lang.Short)) return INT;
        return OTHER;
    }