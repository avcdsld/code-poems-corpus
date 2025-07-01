def merge(
    left,
    right,
    how="inner",
    on=None,
    left_on=None,
    right_on=None,
    left_index=False,
    right_index=False,
    sort=False,
    suffixes=("_x", "_y"),
    copy=True,
    indicator=False,
    validate=None,
):
    """Database style join, where common columns in "on" are merged.

    Args:
        left: DataFrame.
        right: DataFrame.
        how: What type of join to use.
        on: The common column name(s) to join on. If None, and left_on and
            right_on  are also None, will default to all commonly named
            columns.
        left_on: The column(s) on the left to use for the join.
        right_on: The column(s) on the right to use for the join.
        left_index: Use the index from the left as the join keys.
        right_index: Use the index from the right as the join keys.
        sort: Sort the join keys lexicographically in the result.
        suffixes: Add this suffix to the common names not in the "on".
        copy: Does nothing in our implementation
        indicator: Adds a column named _merge to the DataFrame with
            metadata from the merge about each row.
        validate: Checks if merge is a specific type.

    Returns:
         A merged Dataframe
        """
    if not isinstance(left, DataFrame):
        raise ValueError(
            "can not merge DataFrame with instance of type {}".format(type(right))
        )

    return left.merge(
        right,
        how=how,
        on=on,
        left_on=left_on,
        right_on=right_on,
        left_index=left_index,
        right_index=right_index,
        sort=sort,
        suffixes=suffixes,
        copy=copy,
        indicator=indicator,
        validate=validate,
    )