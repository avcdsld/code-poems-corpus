def load_data_and_labels():
    """Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    pos_path = "./data/rt-polaritydata/rt-polarity.pos"
    neg_path = "./data/rt-polaritydata/rt-polarity.neg"
    if not os.path.exists(pos_path):
        os.system("git clone https://github.com/dennybritz/cnn-text-classification-tf.git")
        os.system('mv cnn-text-classification-tf/data .')
        os.system('rm -rf cnn-text-classification-tf')
    positive_examples = list(open(pos_path).readlines())
    positive_examples = [s.strip() for s in positive_examples]
    negative_examples = list(open(neg_path).readlines())
    negative_examples = [s.strip() for s in negative_examples]
    # Split by words
    x_text = positive_examples + negative_examples
    x_text = [clean_str(sent) for sent in x_text]
    x_text = [s.split(" ") for s in x_text]
    # Generate labels
    positive_labels = [1 for _ in positive_examples]
    negative_labels = [0 for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    return [x_text, y]