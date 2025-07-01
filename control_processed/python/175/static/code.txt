def load(cls, sc, path):
        """
        Load a model from the given path.
        """
        model = cls._load_java(sc, path)
        wrapper =\
            sc._jvm.org.apache.spark.mllib.api.python.PowerIterationClusteringModelWrapper(model)
        return PowerIterationClusteringModel(wrapper)