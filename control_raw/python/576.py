def setSample(self, sample):
        """Set sample points from the population. Should be a RDD"""
        if not isinstance(sample, RDD):
            raise TypeError("samples should be a RDD, received %s" % type(sample))
        self._sample = sample