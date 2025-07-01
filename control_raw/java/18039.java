public INDArray storeAndAllocateNewArray() {
        Preconditions.checkState(variableType == VariableType.VARIABLE, "Unable to allocate and store array for variable of type %s: only" +
                " VARIABLE type variables can be initialized using this method", variableType);

        if(!sameDiff.arrayAlreadyExistsForVarName(varName)){
            long[] shape = getShape();
            INDArray arr = getWeightInitScheme().create(dataType(), shape);
            sameDiff.associateArrayWithVariable(arr, this);
            if(log.isTraceEnabled()){
                log.trace("Generated and stored new array for variable \"{}\": shape {}", getVarName(), Arrays.toString(arr.shape()));
            }
            return arr;
        }

        //Variable type SDVariables: shape should never change (i.e., these are params in the net!)
        INDArray ret = getArr();
        return ret;
    }