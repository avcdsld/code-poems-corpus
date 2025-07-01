def _supervised_evaluation_error_checking(targets, predictions):
    """
    Perform basic error checking for the evaluation metrics. Check
    types and sizes of the inputs.
    """
    _raise_error_if_not_sarray(targets, "targets")
    _raise_error_if_not_sarray(predictions, "predictions")
    if (len(targets) != len(predictions)):
        raise _ToolkitError(
         "Input SArrays 'targets' and 'predictions' must be of the same length.")