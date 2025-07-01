def load(cls, sc, path):
        """Load an IsotonicRegressionModel."""
        java_model = sc._jvm.org.apache.spark.mllib.regression.IsotonicRegressionModel.load(
            sc._jsc.sc(), path)
        py_boundaries = _java2py(sc, java_model.boundaryVector()).toArray()
        py_predictions = _java2py(sc, java_model.predictionVector()).toArray()
        return IsotonicRegressionModel(py_boundaries, py_predictions, java_model.isotonic)