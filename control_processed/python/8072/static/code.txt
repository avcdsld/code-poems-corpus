def remove_absolute_resample__roc_auc(X, y, model_generator, method_name, num_fcounts=11):
    """ Remove Absolute (resample)
    xlabel = "Max fraction of features removed"
    ylabel = "1 - ROC AUC"
    transform = "one_minus"
    sort_order = 15
    """
    return __run_measure(measures.remove_resample, X, y, model_generator, method_name, 0, num_fcounts, sklearn.metrics.roc_auc_score)