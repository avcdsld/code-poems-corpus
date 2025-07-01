def multi_log_probs_from_logits_and_actions(policy_logits, actions):
    """Computes action log-probs from policy logits and actions.

  In the notation used throughout documentation and comments, T refers to the
  time dimension ranging from 0 to T-1. B refers to the batch size and
  ACTION_SPACE refers to the list of numbers each representing a number of
  actions.

  Args:
    policy_logits: A list with length of ACTION_SPACE of float32
      tensors of shapes
      [T, B, ACTION_SPACE[0]],
      ...,
      [T, B, ACTION_SPACE[-1]]
      with un-normalized log-probabilities parameterizing a softmax policy.
    actions: A list with length of ACTION_SPACE of int32
      tensors of shapes
      [T, B],
      ...,
      [T, B]
      with actions.

  Returns:
    A list with length of ACTION_SPACE of float32
      tensors of shapes
      [T, B],
      ...,
      [T, B]
      corresponding to the sampling log probability
      of the chosen action w.r.t. the policy.
  """

    log_probs = []
    for i in range(len(policy_logits)):
        log_probs.append(-tf.nn.sparse_softmax_cross_entropy_with_logits(
            logits=policy_logits[i], labels=actions[i]))

    return log_probs