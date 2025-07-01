def load_dataset(data_name):
    """Load sentiment dataset."""
    if data_name == 'MR' or data_name == 'Subj':
        train_dataset, output_size = _load_file(data_name)
        vocab, max_len = _build_vocab(data_name, train_dataset, [])
        train_dataset, train_data_lengths = _preprocess_dataset(train_dataset, vocab, max_len)
        return vocab, max_len, output_size, train_dataset, train_data_lengths
    else:
        train_dataset, test_dataset, output_size = _load_file(data_name)
        vocab, max_len = _build_vocab(data_name, train_dataset, test_dataset)
        train_dataset, train_data_lengths = _preprocess_dataset(train_dataset, vocab, max_len)
        test_dataset, test_data_lengths = _preprocess_dataset(test_dataset, vocab, max_len)
        return vocab, max_len, output_size, train_dataset, train_data_lengths, test_dataset, \
               test_data_lengths