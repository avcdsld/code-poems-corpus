def ChunkedAttentionSelector(x, params, selector=None, **kwargs):
  """Select which chunks to attend to in chunked attention.

  Args:
    x: inputs, a list of elements of the form (q, k, v), mask for each chunk.
    params: parameters (unused).
    selector: a function from chunk_number -> list of chunk numbers that says
      which other chunks should be appended to the given one (previous if None).
    **kwargs: unused other arguments.

  Returns:
    a list of elements of the form (q, k', v'), mask' where k', v' and mask' are
    concatenations of k, v and identity-extended masks from selected chunks.
  """
  del params, kwargs
  selector = selector or (lambda x: [] if x < 1 else [x-1])
  triples, masks = zip(*x)
  (queries, keys, values) = zip(*triples)
  result = []
  for i in range(len(x)):
    selected = selector(i)
    # Since keys and values are [batch, length, depth] we concatenate on axis=1.
    # We also always include the current key or value at the end.
    new_key_list = [keys[j] for j in selected]
    new_key = np.concatenate(new_key_list + [keys[i]], axis=1)
    new_value = np.concatenate(
        [values[j] for j in selected] + [values[i]], axis=1)
    # Masks are (1, query-len, key-len) so we concatenate on axis=2.
    new_mask_shapes = [(1, queries[i].shape[1], key.shape[1])
                       for key in new_key_list]
    cur_mask = masks[i]
    # Masks are all-1 for the added chunks (no masking).
    new_mask_list = [np.ones(s, dtype=cur_mask.dtype) for s in new_mask_shapes]
    # We still use the current (often causal) mask for the final chunk.
    new_mask = np.concatenate(new_mask_list + [cur_mask], axis=2)
    result.append(((queries[i], new_key, new_value), new_mask))
  return tuple(result)