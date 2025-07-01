public SDVariable reverseSequence(String name, SDVariable x, SDVariable seq_lengths, int seqDim, int batchDim) {
        SDVariable ret = f().reverseSequence(x, seq_lengths, seqDim, batchDim);
        return updateVariableNameAndReference(ret, name);
    }