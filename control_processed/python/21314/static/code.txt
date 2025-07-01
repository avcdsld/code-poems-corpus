def computePreRec(cm, class_names):
    '''
    This function computes the precision, recall and f1 measures,
    given a confusion matrix
    '''
    n_classes = cm.shape[0]
    if len(class_names) != n_classes:
        print("Error in computePreRec! Confusion matrix and class_names "
              "list must be of the same size!")
        return
    precision = []
    recall = []
    f1 = []    
    for i, c in enumerate(class_names):
        precision.append(cm[i,i] / numpy.sum(cm[:,i]))
        recall.append(cm[i,i] / numpy.sum(cm[i,:]))
        f1.append( 2 * precision[-1] * recall[-1] / (precision[-1] + recall[-1]))
    return recall, precision, f1