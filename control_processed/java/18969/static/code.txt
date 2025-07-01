public static String getModuleNameFor(Op op) {
        //String functionName = op instanceof TransformOp || op instanceof ReduceOp || op instanceof IndexAccumulation ? op.opName() + "_strided" : op.opName();
        String moduleName = null;
        if (op instanceof ReduceOp) {

            moduleName = "reduce";

            // FIXME: special case for reduce3
            if (op.opName().equals("cosinesimilarity")) {
                moduleName = "reduce3";
            } else if (op.opName().equals("euclidean")) {
                moduleName = "reduce3";
            } else if (op.opName().equals("manhattan")) {
                moduleName = "reduce3";
            }

        } else if (op instanceof TransformOp) {
            // FIXME: we need special case for pairwise transforms for now. Later we should make them separate kernel call
            if (op.opName().equals("add")) {
                moduleName = "pairWiseTransform";
            } else if (op.opName().equals("copy")) {
                moduleName = "pairWiseTransform";
            } else if (op.opName().equals("div")) {
                moduleName = "pairWiseTransform";
            } else if (op.opName().equals("mul")) {
                moduleName = "pairWiseTransform";
            } else if (op.opName().equals("rdiv")) {
                moduleName = "pairWiseTransform";
            } else if (op.opName().equals("rsub")) {
                moduleName = "pairWiseTransform";
            } else if (op.opName().equals("sub")) {
                moduleName = "pairWiseTransform";

            } else {
                moduleName = "transform";
            }
        } else if (op instanceof ScalarOp) {
            moduleName = "scalar";
        } else if (op instanceof BroadcastOp) {
            moduleName = "broadcast";
        } else if (op instanceof IndexAccumulation) {
            moduleName = "indexReduce";
        }
        return moduleName;
    }