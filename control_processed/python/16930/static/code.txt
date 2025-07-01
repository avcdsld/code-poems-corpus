def _raise_error_if_sframe_empty(dataset, variable_name="SFrame"):
    """
    Check if the input is empty.
    """
    err_msg = "Input %s either has no rows or no columns. A non-empty SFrame "
    err_msg += "is required."

    if dataset.num_rows() == 0 or dataset.num_columns() == 0:
        raise ToolkitError(err_msg % variable_name)