def epochs(steps=None, epoch_steps=1):
  """Iterator over epochs until steps is reached. 1-indexed.

  Args:
    steps: int, total number of steps. Infinite if None.
    epoch_steps: int, number of steps per epoch. Can also be an iterable<int> to
      enable variable length epochs.

  Yields:
    (epoch: int, epoch id, epoch_steps: int, number of steps in this epoch)
  """
  try:
    iter(epoch_steps)
  except TypeError:
    epoch_steps = itertools.repeat(epoch_steps)

  step = 0
  for epoch, epoch_steps in enumerate(epoch_steps):
    epoch_steps = min(epoch_steps, steps - step)
    yield (epoch + 1, epoch_steps)
    step += epoch_steps
    if steps and step >= steps:
      break