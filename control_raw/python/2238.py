def _result_type_many(*arrays_and_dtypes):
    """ wrapper around numpy.result_type which overcomes the NPY_MAXARGS (32)
    argument limit """
    try:
        return np.result_type(*arrays_and_dtypes)
    except ValueError:
        # we have > NPY_MAXARGS terms in our expression
        return reduce(np.result_type, arrays_and_dtypes)