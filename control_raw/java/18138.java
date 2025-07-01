public List<String> outputs(){
        List<String> out = new ArrayList<>();
        for(Variable v : variables.values()){
            if(v.getVariable().isConstant() || v.getVariable().isPlaceHolder() ||                   //Exclude constants and placeholders
                    (v.getInputsForOp() != null && !v.getInputsForOp().isEmpty()) ||                //Exclude variables that are inputs to ops
                    (v.getControlDepsForOp() != null && !v.getControlDepsForOp().isEmpty()) ||      //Exclude variables that are control dependency inputs to ops
                    (v.getControlDepsForVar() != null && !v.getControlDepsForVar().isEmpty())) {    //Exclude variables that are control dependency inputs to other variables (mainly for import of cond etc ops)
                continue;
            }

            //Also exclude assert etc ops - doesn't make sense to return these "outputs" to user
            if(v.getOutputOfOp() != null){
                String opName = v.getOutputOfOp();
                SameDiffOp o = ops.get(opName);
                if(o.getOp() instanceof Assert){
                    continue;
                }

                //A bit of a hack for TF import: some TF graphs have Switch ops, where the output of one branch isn't consumed
                // by any ops. Consequently, during execution this "output" might never be available. So we'll exclude the output of execution here
                if(o.getOp() instanceof Switch){
                    continue;
                }
            }


            out.add(v.getName());
        }
        return out;
    }