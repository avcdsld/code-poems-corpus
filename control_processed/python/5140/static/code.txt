def pack_examples(examples,
                  has_inputs,
                  packed_length=256,
                  spacing=2,
                  queue_size=10,
                  chop_long_sequences=False):
  """Pack examples into longer examples.

  If has_inputs=False, we are packing single-sequence examples with
  targets only and no inputs.

  In this case, we concatenate the targets from several examples to form
  each new example.  We insert a number of zeros for spacing between the
  original sequences.  This is to help the sequences stay separate
  under convolutions.  If chop_long_sequences is set, then any input sequence
  longer than packed_length gets chopped up into multiple examples.  Otherwise,
  long sequences are emitted as singletons.

  If has_inputs=True, then we are packing sequence-to-sequence
  examples.  We combine several examples by concatenating the inputs
  (as above) and concatenating the targets (as above).  Chopping of
  long sequences is not supported.

  The packed examples are represented as dictionaries containing:
    "inputs", "targets": the packed sequences described above
    "inputs_segmentation", "targets_segmentation":
       Sequences aligned with "inputs", "targets" specifying to which original
       sequence each position belongs.  Numbering starts from 1, and 0 is used
       for spacing.  This information is useful for preventing attention across
       segments.
       e.g. [1 1 1 1 1 1 0 0 2 2 2 0 0 3 3 3 3 3 0 0 4 4 4]
     "inputs_position", "targets_position":
       Sequences aligned with "inputs", "targets" specifying position within
       the original sequence.  This is useful for positional encodings.
       e.g. [0 1 2 3 4 5 0 0 0 1 2 0 0 0 1 2 3 4 0 0 0 1 2]

  Args:
    examples: a generator returning feature dictionaries.
    has_inputs: a boolean
    packed_length: an integer
    spacing: an integer
    queue_size: an integer
    chop_long_sequences: a boolean

  Yields:
    feature dictionaries.
  """
  packer = SequencePairPacker if has_inputs else SequencePacker
  combined = []
  for example in examples:
    x = ((example["inputs"], example["targets"])
         if has_inputs else example["targets"])
    if chop_long_sequences and len(x) > packed_length:
      assert not has_inputs
      num_fragments = len(x) // packed_length
      for i in range(num_fragments):
        yield packer(
            x[packed_length * i:packed_length * (i + 1)], spacing).to_dict()
      x = x[packed_length * num_fragments:]
    added = False
    for c in combined:
      if c.can_fit(x, packed_length):
        c.add(x)
        added = True
        break
    if not added:
      if len(combined) == queue_size:
        yield combined[0].to_dict()
        combined = combined[1:]
      combined.append(packer(x, spacing))
  for c in combined:
    yield c.to_dict()