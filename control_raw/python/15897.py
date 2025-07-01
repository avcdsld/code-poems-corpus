def evaluate_regressor(model, data, target="target", verbose=False):
    """
    Evaluate a CoreML regression model and compare against predictions
    from the original framework (for testing correctness of conversion)

    Parameters
    ----------
    filename: [str | MLModel]
        File path from which to load the MLModel from (OR) a loaded version of
        MLModel.

    data: [str | Dataframe]
        Test data on which to evaluate the models (dataframe,
        or path to a .csv file).

    target: str
       Name of the column in the dataframe that must be interpreted
       as the target column.

    verbose: bool
       Set to true for a more verbose output.

    See Also
    --------
    evaluate_classifier

    Examples
    --------
    .. sourcecode:: python

        >>> metrics = coremltools.utils.evaluate_regressor(spec, 'data_and_predictions.csv', 'target')
        >>> print(metrics)
        {"samples": 10, "rmse": 0.0, max_error: 0.0}
    """
    model = _get_model(model)

    if verbose:
        print("")
        print("Other Framework\t\tPredicted\t\tDelta")

    max_error = 0
    error_squared = 0

    for index,row in data.iterrows():
        predicted = model.predict(dict(row))[_to_unicode(target)]
        other_framework = row["prediction"]
        delta = predicted - other_framework

        if verbose:
            print("%s\t\t\t\t%s\t\t\t%0.4f" % (other_framework, predicted, delta))

        max_error = max(abs(delta), max_error)
        error_squared = error_squared + (delta * delta)

    ret = {
        "samples": len(data),
        "rmse": _math.sqrt(error_squared / len(data)),
        "max_error": max_error
    }

    if verbose:
        print("results: %s" % ret)
    return ret