@SuppressWarnings("unused") // called through reflection by RequestServer
  public ModelMetricsListSchemaV3 score(int version, ModelMetricsListSchemaV3 s) {
    // parameters checking:
    if (null == s.model) throw new H2OIllegalArgumentException("model", "predict", s.model);
    if (null == DKV.get(s.model.name)) throw new H2OKeyNotFoundArgumentException("model", "predict", s.model.name);

    if (null == s.frame) throw new H2OIllegalArgumentException("frame", "predict", s.frame);
    if (null == DKV.get(s.frame.name)) throw new H2OKeyNotFoundArgumentException("frame", "predict", s.frame.name);

    ModelMetricsList parms = s.createAndFillImpl();

    String customMetricFunc = s.custom_metric_func;
    if (customMetricFunc == null) {
      customMetricFunc = parms._model._parms._custom_metric_func;
    }
    parms._model.score(parms._frame, parms._predictions_name, null, true, CFuncRef.from(customMetricFunc)).remove(); // throw away predictions, keep metrics as a side-effect
    ModelMetricsListSchemaV3 mm = this.fetch(version, s);

    // TODO: for now only binary predictors write an MM object.
    // For the others cons one up here to return the predictions frame.
    if (null == mm)
      mm = new ModelMetricsListSchemaV3();

    if (null == mm.model_metrics || 0 == mm.model_metrics.length) {
      Log.warn("Score() did not return a ModelMetrics for model: " + s.model + " on frame: " + s.frame);
    }

    return mm;
  }