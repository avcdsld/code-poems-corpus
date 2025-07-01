protected static void validateFloatingPoint(String opName, SDVariable v) {
        if (v == null)
            return;
        if (!v.dataType().isFPType())
            throw new IllegalStateException("Cannot apply operation \"" + opName + "\" to variable \"" + v.getVarName() + "\" with non-floating point data type " + v.dataType());
    }