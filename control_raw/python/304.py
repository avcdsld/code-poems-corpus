def train(cls, data, lambda_=1.0):
        """
        Train a Naive Bayes model given an RDD of (label, features)
        vectors.

        This is the Multinomial NB (U{http://tinyurl.com/lsdw6p}) which
        can handle all kinds of discrete data.  For example, by
        converting documents into TF-IDF vectors, it can be used for
        document classification. By making every vector a 0-1 vector,
        it can also be used as Bernoulli NB (U{http://tinyurl.com/p7c96j6}).
        The input feature values must be nonnegative.

        :param data:
          RDD of LabeledPoint.
        :param lambda_:
          The smoothing parameter.
          (default: 1.0)
        """
        first = data.first()
        if not isinstance(first, LabeledPoint):
            raise ValueError("`data` should be an RDD of LabeledPoint")
        labels, pi, theta = callMLlibFunc("trainNaiveBayesModel", data, lambda_)
        return NaiveBayesModel(labels.toArray(), pi.toArray(), numpy.array(theta))