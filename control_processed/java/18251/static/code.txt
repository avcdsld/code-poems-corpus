public INDArray[] output(long graphId, Pair<String, INDArray>... inputs) {
        val operands = new Operands();
        for (val in:inputs)
            operands.addArgument(in.getFirst(), in.getSecond());

        return output(graphId, operands).asArray();
    }