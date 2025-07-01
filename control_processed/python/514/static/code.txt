def undefinedImageType(self):
        """
        Returns the name of undefined image type for the invalid image.

        .. versionadded:: 2.3.0
        """

        if self._undefinedImageType is None:
            ctx = SparkContext._active_spark_context
            self._undefinedImageType = \
                ctx._jvm.org.apache.spark.ml.image.ImageSchema.undefinedImageType()
        return self._undefinedImageType