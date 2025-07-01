public double calcRegularizationScore() {
        Preconditions.checkState(trainingConfig != null, "No training configuration has been set. A training configuration must " +
                "be set before calculating the L2 loss. Use setTrainingConfig(TrainingConfig)");

        if(trainingConfig.getRegularization() == null || trainingConfig.getRegularization().isEmpty()){
            return 0.0;
        }

        if(trainingConfig.getTrainableParams() == null || trainingConfig.getTrainableParams().isEmpty())
            initializeTraining();

        List<Regularization> l = trainingConfig.getRegularization();
        double loss = 0.0;
        for (String s : trainingConfig.getTrainableParams()) {
            for(Regularization r : l){
                INDArray arr = getVariable(s).getArr();
                loss += r.score(arr, trainingConfig.getIterationCount(), trainingConfig.getEpochCount());
            }
        }
        return loss;
    }