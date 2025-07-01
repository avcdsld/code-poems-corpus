def pick_probability(x, temp, cos_distance):
    """Row normalized exponentiated pairwise distance between all the elements
    of x. Conceptualized as the probability of sampling a neighbor point for
    every element of x, proportional to the distance between the points.
    :param x: a matrix
    :param temp: Temperature
    :cos_distance: Boolean for using cosine or euclidean distance

    :returns: A tensor for the row normalized exponentiated pairwise distance
              between all the elements of x.
    """
    f = SNNLCrossEntropy.fits(
        x, x, temp, cos_distance) - tf.eye(tf.shape(x)[0])
    return f / (
        SNNLCrossEntropy.STABILITY_EPS + tf.expand_dims(tf.reduce_sum(f, 1), 1))