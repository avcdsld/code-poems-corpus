@Override protected void toJavaUnifyPreds(SBPrintStream body) {
    // Preds are filled in from the trees, but need to be adjusted according to
    // the loss function.
    if( _parms._distribution == DistributionFamily.bernoulli
        || _parms._distribution == DistributionFamily.quasibinomial
        || _parms._distribution == DistributionFamily.modified_huber
        ) {
      body.ip("preds[2] = preds[1] + ").p(_output._init_f).p(";").nl();
      body.ip("preds[2] = " + new Distribution(_parms).linkInvString("preds[2]") + ";").nl();
      body.ip("preds[1] = 1.0-preds[2];").nl();
      if (_parms._balance_classes)
        body.ip("hex.genmodel.GenModel.correctProbabilities(preds, PRIOR_CLASS_DISTRIB, MODEL_CLASS_DISTRIB);").nl();
      body.ip("preds[0] = hex.genmodel.GenModel.getPrediction(preds, PRIOR_CLASS_DISTRIB, data, " + defaultThreshold() + ");").nl();
      return;
    }
    if( _output.nclasses() == 1 ) { // Regression
      body.ip("preds[0] += ").p(_output._init_f).p(";").nl();
      body.ip("preds[0] = " + new Distribution(_parms).linkInvString("preds[0]") + ";").nl();
      return;
    }
    if( _output.nclasses()==2 ) { // Kept the initial prediction for binomial
      body.ip("preds[1] += ").p(_output._init_f).p(";").nl();
      body.ip("preds[2] = - preds[1];").nl();
    }
    body.ip("hex.genmodel.GenModel.GBM_rescale(preds);").nl();
    if (_parms._balance_classes)
      body.ip("hex.genmodel.GenModel.correctProbabilities(preds, PRIOR_CLASS_DISTRIB, MODEL_CLASS_DISTRIB);").nl();
    body.ip("preds[0] = hex.genmodel.GenModel.getPrediction(preds, PRIOR_CLASS_DISTRIB, data, " + defaultThreshold() + ");").nl();
  }