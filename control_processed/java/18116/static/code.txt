public void associateArrayWithVariable(INDArray arr, SDVariable variable) {
        if (variable == null) {
            throw new ND4JIllegalArgumentException("Variable must not be null!");
        }
        if (arr == null) {
            throw new ND4JIllegalArgumentException("Array must not be null");
        }

        if (variable.dataType() != arr.dataType())
            arr = arr.castTo(variable.dataType());

        Preconditions.checkState(variable.dataType() == arr.dataType(), "Variable \"%s\" has datatype %s: cannot associate array with type %s with this variable",
                variable.getVarName(), variable.dataType(), arr.dataType());

        // FIXME: remove this before release
        if (sessions.get(Thread.currentThread().getId()) == null) {
            sessions.put(Thread.currentThread().getId(), new InferenceSession(this));
        }

        boolean duped = false;
        if(arr.isAttached()) {
            arr = arr.detach();
            duped = true;
        }
        if(arr.isView()) {
            arr = arr.dup();
            duped = true;
        }

        if(!duped && variable.getVariableType() == VariableType.VARIABLE) {
            for (DeviceLocalNDArray otherArr : variablesArrays.values()) {
                if (otherArr.get() == arr) {    //Check for exact same object, to avoid array reuse (can result in unexpected behaviour)
                    arr = arr.dup();
                    break;
                }
            }
        }

        switch(variable.getVariableType()){
            case VARIABLE:
                variablesArrays.put(variable.getVarName(), new DeviceLocalNDArray(arr));
                break;
            case CONSTANT:
                constantArrays.put(variable.getVarName(), new DeviceLocalNDArray(arr));
                break;
            case ARRAY:
                // FIXME: remove this before release
                val session = sessions.get(Thread.currentThread().getId());
                val varId = session.newVarId(variable.getVarName(), AbstractSession.OUTER_FRAME, 0, null);
                session.getNodeOutputs().put(varId, arr);
                //throw new UnsupportedOperationException("Cannot associate array with SDVariable of type ARRAY");
            case PLACEHOLDER:
                long tid = Thread.currentThread().getId();
                if(!placeholdersPerThread.containsKey(tid)){
                    placeholdersPerThread.put(tid, new HashMap<String, INDArray>());
                }
                placeholdersPerThread.get(tid).put(variable.getVarName(), arr);
                break;
            default:
                throw new IllegalStateException("Unknown variable type: " + variable.getVariableType());
        }

        //putOrUpdateShapeForVarName(variable.getVarName(), arr.shape(), true);

        //Also update nested SameDiff instances (such as gradient function)
        if(sameDiffFunctionInstances != null && sameDiffFunctionInstances.size() > 0){
            for(Map.Entry<String,SameDiff> e : sameDiffFunctionInstances.entrySet()){
                SameDiff sd = e.getValue();
                SDVariable v = sd.getVariable(variable.getVarName());
                if(v != null){
                    sd.associateArrayWithVariable(arr, v);
                }
            }
        }
    }