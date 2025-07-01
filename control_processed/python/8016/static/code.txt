def independentlinear60(display=False):
    """ A simulated dataset with tight correlations among distinct groups of features.
    """

    # set a constant seed
    old_seed = np.random.seed()
    np.random.seed(0)

    # generate dataset with known correlation
    N = 1000
    M = 60

    # set one coefficent from each group of 3 to 1
    beta = np.zeros(M)
    beta[0:30:3] = 1
    f = lambda X: np.matmul(X, beta)

    # Make sure the sample correlation is a perfect match
    X_start = np.random.randn(N, M)
    X = X_start - X_start.mean(0)
    y = f(X) + np.random.randn(N) * 1e-2

    # restore the previous numpy random seed
    np.random.seed(old_seed)

    return pd.DataFrame(X), y