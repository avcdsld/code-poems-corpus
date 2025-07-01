def cache_key(working_directory, arguments, configure_kwargs):
  """Compute a `TensorBoardInfo.cache_key` field.

  The format returned by this function is opaque. Clients may only
  inspect it by comparing it for equality with other results from this
  function.

  Args:
    working_directory: The directory from which TensorBoard was launched
      and relative to which paths like `--logdir` and `--db` are
      resolved.
    arguments: The command-line args to TensorBoard, as `sys.argv[1:]`.
      Should be a list (or tuple), not an unparsed string. If you have a
      raw shell command, use `shlex.split` before passing it to this
      function.
    configure_kwargs: A dictionary of additional argument values to
      override the textual `arguments`, with the same semantics as in
      `tensorboard.program.TensorBoard.configure`. May be an empty
      dictionary.

  Returns:
    A string such that if two (prospective or actual) TensorBoard
    invocations have the same cache key then it is safe to use one in
    place of the other. The converse is not guaranteed: it is often safe
    to change the order of TensorBoard arguments, or to explicitly set
    them to their default values, or to move them between `arguments`
    and `configure_kwargs`, but such invocations may yield distinct
    cache keys.
  """
  if not isinstance(arguments, (list, tuple)):
    raise TypeError(
        "'arguments' should be a list of arguments, but found: %r "
        "(use `shlex.split` if given a string)"
        % (arguments,)
    )
  datum = {
      "working_directory": working_directory,
      "arguments": arguments,
      "configure_kwargs": configure_kwargs,
  }
  raw = base64.b64encode(
      json.dumps(datum, sort_keys=True, separators=(",", ":")).encode("utf-8")
  )
  # `raw` is of type `bytes`, even though it only contains ASCII
  # characters; we want it to be `str` in both Python 2 and 3.
  return str(raw.decode("ascii"))