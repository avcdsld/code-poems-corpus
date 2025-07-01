public void addOutgoingFor(String[] varNames, DifferentialFunction function) {

        if (function.getOwnName() == null)
            throw new ND4JIllegalStateException("Instance id can not be null. Function not initialized properly");


        if (ops.get(function.getOwnName()).getOutputsOfOp() != null && !ops.get(function.getOwnName()).getOutputsOfOp().isEmpty()) {
            throw new ND4JIllegalStateException("Outgoing arguments already declared for " + function);
        }

        if (varNames == null)
            throw new ND4JIllegalStateException("Var names can not be null!");


        for (int i = 0; i < varNames.length; i++) {
            if (varNames[i] == null)
                throw new ND4JIllegalStateException("Variable name elements can not be null!");
        }

        ops.get(function.getOwnName()).setOutputsOfOp(Arrays.asList(varNames));

        for (String resultName : varNames) {
            variables.get(resultName).setOutputOfOp(function.getOwnName());
        }
    }