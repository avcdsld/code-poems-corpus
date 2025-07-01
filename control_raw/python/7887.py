def build_iters(data_dir, max_records, train_fraction, batch_size, buckets=None):
    """
    Reads a csv of sentences/tag sequences into a pandas dataframe.
    Converts into X = array(list(int)) & Y = array(list(int))
    Splits into training and test sets
    Builds dictionaries mapping from index labels to labels/ indexed features to features
    :param data_dir: directory to read in csv data from
    :param max_records: total number of records to randomly select from input data
    :param train_fraction: fraction of the data to use for training
    :param batch_size: records in mini-batches during training
    :param buckets: size of each bucket in the iterators
    :return: train_iter, val_iter, word_to_index, index_to_word, pos_to_index, index_to_pos
    """
    # Read in data as numpy array
    df = pd.read_pickle(os.path.join(data_dir, "ner_data.pkl"))[:max_records]

    # Get feature lists
    entities=[list(array) for array in df["BILOU_tag"].values]
    sentences = [list(array) for array in df["token"].values]
    chars=[[[c for c in word] for word in sentence] for sentence in sentences]

    # Build vocabularies
    entity_to_index, index_to_entity = build_vocab(entities)
    word_to_index, index_to_word = build_vocab(sentences)
    char_to_index, index_to_char = build_vocab([np.array([c for c in word]) for word in index_to_word])
    save_obj(entity_to_index, os.path.join(args.data_dir, "tag_to_index"))

    # Map strings to integer values
    indexed_entities=[list(map(entity_to_index.get, l)) for l in entities]
    indexed_tokens=[list(map(word_to_index.get, l)) for l in sentences]
    indexed_chars=[[list(map(char_to_index.get, word)) for word in sentence] for sentence in chars]

    # Split into training and testing data
    idx=int(len(indexed_tokens)*train_fraction)
    X_token_train, X_char_train, Y_train = indexed_tokens[:idx], indexed_chars[:idx], indexed_entities[:idx]
    X_token_test, X_char_test, Y_test = indexed_tokens[idx:], indexed_chars[idx:], indexed_entities[idx:]

    # build iterators to feed batches to network
    train_iter = iterators.BucketNerIter(sentences=X_token_train, characters=X_char_train, label=Y_train,
                                         max_token_chars=5, batch_size=batch_size, buckets=buckets)
    val_iter = iterators.BucketNerIter(sentences=X_token_test, characters=X_char_test, label=Y_test,
                                         max_token_chars=train_iter.max_token_chars, batch_size=batch_size, buckets=train_iter.buckets)
    return train_iter, val_iter, word_to_index, char_to_index, entity_to_index