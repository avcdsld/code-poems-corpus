def split_result_of_axis_func_pandas(axis, num_splits, result, length_list=None):
    """Split the Pandas result evenly based on the provided number of splits.

    Args:
        axis: The axis to split across.
        num_splits: The number of even splits to create.
        result: The result of the computation. This should be a Pandas
            DataFrame.
        length_list: The list of lengths to split this DataFrame into. This is used to
            return the DataFrame to its original partitioning schema.

    Returns:
        A list of Pandas DataFrames.
    """
    if num_splits == 1:
        return result
    if length_list is not None:
        length_list.insert(0, 0)
        sums = np.cumsum(length_list)
        if axis == 0:
            return [result.iloc[sums[i] : sums[i + 1]] for i in range(len(sums) - 1)]
        else:
            return [result.iloc[:, sums[i] : sums[i + 1]] for i in range(len(sums) - 1)]
    # We do this to restore block partitioning
    chunksize = compute_chunksize(result, num_splits, axis=axis)
    if axis == 0:
        return [
            result.iloc[chunksize * i : chunksize * (i + 1)] for i in range(num_splits)
        ]
    else:
        return [
            result.iloc[:, chunksize * i : chunksize * (i + 1)]
            for i in range(num_splits)
        ]