def predict_input(itos_filename, trained_classifier_filename, num_classes=2):
    """
    Loads a model and produces predictions on arbitrary input.
    :param itos_filename: the path to the id-to-string mapping file
    :param trained_classifier_filename: the filename of the trained classifier;
                                        typically ends with "clas_1.h5"
    :param num_classes: the number of classes that the model predicts
    """
    # Check the itos file exists
    if not os.path.exists(itos_filename):
        print("Could not find " + itos_filename)
        exit(-1)

    # Check the classifier file exists
    if not os.path.exists(trained_classifier_filename):
        print("Could not find " + trained_classifier_filename)
        exit(-1)

    stoi, model = load_model(itos_filename, trained_classifier_filename, num_classes)

    while True:
        text = input("Enter text to analyse (or q to quit): ")
        if text.strip() == 'q':
            break
        else:
            scores = predict_text(stoi, model, text)
            print("Result id {0}, Scores: {1}".format(np.argmax(scores), scores))