def _raise_error_if_not_drawing_classifier_input_sframe(
    dataset, feature, target):
    """
    Performs some sanity checks on the SFrame provided as input to 
    `turicreate.drawing_classifier.create` and raises a ToolkitError
    if something in the dataset is missing or wrong.
    """
    from turicreate.toolkits._internal_utils import _raise_error_if_not_sframe
    _raise_error_if_not_sframe(dataset)
    if feature not in dataset.column_names():
        raise _ToolkitError("Feature column '%s' does not exist" % feature)
    if target not in dataset.column_names():
        raise _ToolkitError("Target column '%s' does not exist" % target)
    if (dataset[feature].dtype != _tc.Image and dataset[feature].dtype != list):
        raise _ToolkitError("Feature column must contain images" 
            + " or stroke-based drawings encoded as lists of strokes" 
            + " where each stroke is a list of points and" 
            + " each point is stored as a dictionary")
    if dataset[target].dtype != int and dataset[target].dtype != str:
        raise _ToolkitError("Target column contains " + str(dataset[target].dtype)
            + " but it must contain strings or integers to represent" 
            + " labels for drawings.")
    if len(dataset) == 0:
        raise _ToolkitError("Input Dataset is empty!")