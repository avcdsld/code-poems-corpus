protected synchronized void fit(MultiDataSetIterator iter, int numEpochs, boolean incrementEpochCount){
        Preconditions.checkNotNull(iter, "Iterator must not be null");
        Preconditions.checkState(numEpochs > 0, "Number of training epochs must be a positive number. Got: %s", numEpochs);
        Preconditions.checkState(trainingConfig != null, "No training configuration has been set. A training configuration must " +
                "be set before training. Use setTrainingConfig(TrainingConfig)");
        Preconditions.checkState(numEpochs == 1 || iter.resetSupported(), "Cannot train for multiple epochs on an iterator that" +
                " does not support resetting");

        if(!iter.hasNext() && iter.resetSupported())
            iter.reset();

        boolean performedValidation = false;

        for(int i = 0; i < numEpochs; i++) {
            while (iter.hasNext()) {
                org.nd4j.linalg.dataset.api.MultiDataSet ds = iter.next();
                if(!performedValidation){
                    Preconditions.checkState(trainingConfig.getDataSetFeatureMapping().size() == ds.numFeatureArrays(),
                            "The number of dataset feature mapping variables set in the training configuration (%s) must match" +
                                    " the number of dataset feature arrays (%s)", trainingConfig.getDataSetFeatureMapping().size(), ds.numFeatureArrays());
                    List<String> labelMapping = trainingConfig.getDataSetLabelMapping();
                    int lblSize = labelMapping == null ? 0 : labelMapping.size();
                    Preconditions.checkState(lblSize == ds.numLabelsArrays(),
                            "The number of dataset label mapping variables set in the training configuration (%s) must match" +
                                    " the number of dataset label arrays (%s)", lblSize, ds.numLabelsArrays());

                    performedValidation = true;
                }

                //Create placeholder variable map
                Map<String, INDArray> placeholders = toPlaceholderMap(ds);

                Preconditions.checkState(placeholders.size() > 0, "No placeholder variables were set for training");
                resolveVariablesWith(placeholders);

                //Calculate gradients:
                execBackwards(placeholders);


                //Apply updater:
                if (!initializedTraining)
                    initializeTraining();

                int iteration = trainingConfig.getIterationCount();
                int e = trainingConfig.getEpochCount();
                for (String s : trainingConfig.getTrainableParams()) {
                    //TODO fix using inference session
                    INDArray param = variables.get(s).getVariable().getArr();
                    SDVariable gradVar = variables.get(s).getVariable().getGradient();
                    if(gradVar == null){
                        //Not all trainable parameters have gradients defined.
                        //Consider graph: in1->loss1; in2->loss2, where we optimize only loss1.
                        //No gradient will be present for in2, because in2 doesn't impact loss1 at all
                        continue;
                    }
                    INDArray grad = gradVar.getArr();
                    //Note: don't need to divide by minibatch - that should be handled in loss function and hence loss function gradients,
                    // which should flow through to here

                    //Pre-apply regularization (L1, L2)
                    List<Regularization> r = trainingConfig.getRegularization();
                    int iterCount = trainingConfig.getIterationCount();
                    int epochCount = trainingConfig.getEpochCount();
                    double lr = trainingConfig.getUpdater().hasLearningRate() ? trainingConfig.getUpdater().getLearningRate(iteration, epochCount) : 1.0;
                    if(r != null && r.size() > 0){
                        for(Regularization reg : r){
                            if(reg.applyStep() == Regularization.ApplyStep.BEFORE_UPDATER){
                                reg.apply(param, grad, lr, iterCount, epochCount);
                            }
                        }
                    }

                    //Apply updater. Note that we need to reshape to [1,length] for updater
                    INDArray reshapedView = Shape.newShapeNoCopy(grad, new long[]{1, grad.length()}, grad.ordering() == 'f');       //TODO make sure we always reshape in same order!
                    Preconditions.checkState(reshapedView != null, "Error reshaping array for parameter \"%s\": array is a view?", s);
                    GradientUpdater u = updaterMap.get(s);
                    try {
                        u.applyUpdater(reshapedView, iteration, e);
                    } catch (Throwable t) {
                        throw new RuntimeException("Error applying updater " + u.getClass().getSimpleName() + " to parameter \"" + s
                                + "\": either parameter size is inconsistent between iterations, or \"" + s + "\" should not be a trainable parameter?", t);
                    }

                    //Post-apply regularization (weight decay)
                    if(r != null && r.size() > 0){
                        for(Regularization reg : r){
                            if(reg.applyStep() == Regularization.ApplyStep.POST_UPDATER){
                                reg.apply(param, grad, lr, iterCount, epochCount);
                            }
                        }
                    }

                    if (trainingConfig.isMinimize()) {
                        param.subi(grad);
                    } else {
                        param.addi(grad);
                    }
                }

                trainingConfig.incrementIterationCount();
            }

            if(i < numEpochs - 1) {
                iter.reset();
            }

            if(incrementEpochCount)
                trainingConfig.incrementEpochCount();
        }
    }