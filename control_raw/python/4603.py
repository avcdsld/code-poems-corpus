def _build_vocab(filename, vocab_path, vocab_size):
  """Reads a file to build a vocabulary of `vocab_size` most common words.

   The vocabulary is sorted by occurrence count and has one word per line.
   Originally from:
   https://github.com/tensorflow/models/blob/master/tutorials/rnn/ptb/reader.py

  Args:
    filename: file to read list of words from.
    vocab_path: path where to save the vocabulary.
    vocab_size: size of the vocabulary to generate.
  """
  data = _read_words(filename)
  counter = collections.Counter(data)
  count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
  words, _ = list(zip(*count_pairs))
  words = words[:vocab_size]
  with open(vocab_path, "w") as f:
    f.write("\n".join(words))