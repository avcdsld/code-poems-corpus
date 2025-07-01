public SDVariable convertToVariable(@NonNull SDVariable constant) {
        Preconditions.checkState(constant.dataType().isFPType(), "Only floating point SDVariables can be converted to variables," +
                " datatype of %s is %s", constant.getVarName(), constant.dataType());
        convertToVariables(Collections.singletonList(constant));
        return constant;
    }