static public ModelMetricsBinomial make(Vec targetClassProbs, Vec actualLabels, String[] domain) {
    Scope.enter();
    Vec _labels = actualLabels.toCategoricalVec();
    if (domain==null) domain = _labels.domain();
    if (_labels == null || targetClassProbs == null)
      throw new IllegalArgumentException("Missing actualLabels or predictedProbs for binomial metrics!");
    if (!targetClassProbs.isNumeric())
      throw new IllegalArgumentException("Predicted probabilities must be numeric per-class probabilities for binomial metrics.");
    if (targetClassProbs.min() < 0 || targetClassProbs.max() > 1)
      throw new IllegalArgumentException("Predicted probabilities must be between 0 and 1 for binomial metrics.");
    if (domain.length!=2)
      throw new IllegalArgumentException("Domain must have 2 class labels, but is " + Arrays.toString(domain) + " for binomial metrics.");
    _labels = _labels.adaptTo(domain);
    if (_labels.cardinality()!=2)
      throw new IllegalArgumentException("Adapted domain must have 2 class labels, but is " + Arrays.toString(_labels.domain()) + " for binomial metrics.");
    Frame predsLabel = new Frame(targetClassProbs);
    predsLabel.add("labels", _labels);
    MetricBuilderBinomial mb = new BinomialMetrics(_labels.domain()).doAll(predsLabel)._mb;
    _labels.remove();
    Frame preds = new Frame(targetClassProbs);
    ModelMetricsBinomial mm = (ModelMetricsBinomial)mb.makeModelMetrics(null, predsLabel, null, preds);
    mm._description = "Computed on user-given predictions and labels, using F1-optimal threshold: " + mm.auc_obj().defaultThreshold() + ".";
    Scope.exit();
    return mm;
  }