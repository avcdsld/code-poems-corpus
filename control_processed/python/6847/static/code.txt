def rae(label, pred):
    """computes the relative absolute error (condensed using standard deviation formula)"""
    numerator = np.mean(np.abs(label - pred), axis=None)
    denominator = np.mean(np.abs(label - np.mean(label, axis=None)), axis=None)
    return numerator / denominator