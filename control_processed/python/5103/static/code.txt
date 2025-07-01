def TransformerEncoder(vocab_size,
                       num_classes=10,
                       feature_depth=512,
                       feedforward_depth=2048,
                       num_layers=6,
                       num_heads=8,
                       dropout=0.1,
                       max_len=2048,
                       mode='train'):
  """Transformer encoder.

  Args:
    vocab_size: int: vocab size
    num_classes: how many classes on output
    feature_depth: int:  depth of embedding
    feedforward_depth: int: depth of feed-forward layer
    num_layers: int: number of encoder/decoder layers
    num_heads: int: number of attention heads
    dropout: float: dropout rate (how much to drop out)
    max_len: int: maximum symbol length for positional encoding
    mode: str: 'train' or 'eval'

  Returns:
    the Transformer encoder layer.
  """
  input_embedding = layers.Serial(
      layers.Embedding(feature_depth, vocab_size),
      layers.Dropout(rate=dropout, mode=mode),
      layers.PositionalEncoding(max_len=max_len)
  )
  return layers.Serial(
      layers.Branch(),  # Branch input to create embedding and mask.
      layers.Parallel(input_embedding, layers.PaddingMask()),
      layers.Serial(*[EncoderLayer(feature_depth, feedforward_depth, num_heads,
                                   dropout, mode)
                      for _ in range(num_layers)]),
      layers.FirstBranch(),  # Drop the mask.
      layers.LayerNorm(),
      layers.Mean(axis=1),  # Average on length.
      layers.Dense(num_classes),
      layers.LogSoftmax()
  )