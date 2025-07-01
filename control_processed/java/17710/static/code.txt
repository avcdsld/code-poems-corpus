public int getPredictedClass(){
        if(predictedClass == -1){
            if(classPredictions.rank() == 1){
                predictedClass = classPredictions.argMax().getInt(0);
            } else {
                // ravel in case we get a column vector, or rank 2 row vector, etc
                predictedClass = classPredictions.ravel().argMax().getInt(0);
            }
        }
        return predictedClass;
    }