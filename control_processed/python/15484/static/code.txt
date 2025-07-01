def try_pick_piece_of_work(self, worker_id, submission_id=None):
    """Tries pick next unclaimed piece of work to do.

    Attempt to claim work piece is done using Cloud Datastore transaction, so
    only one worker can claim any work piece at a time.

    Args:
      worker_id: ID of current worker
      submission_id: if not None then this method will try to pick
        piece of work for this submission

    Returns:
      ID of the claimed work piece
    """
    client = self._datastore_client
    unclaimed_work_ids = None
    if submission_id:
      unclaimed_work_ids = [
          k for k, v in iteritems(self.work)
          if is_unclaimed(v) and (v['submission_id'] == submission_id)
      ]
    if not unclaimed_work_ids:
      unclaimed_work_ids = [k for k, v in iteritems(self.work)
                            if is_unclaimed(v)]
    if unclaimed_work_ids:
      next_work_id = random.choice(unclaimed_work_ids)
    else:
      return None
    try:
      with client.transaction() as transaction:
        work_key = client.key(KIND_WORK_TYPE, self._work_type_entity_id,
                              KIND_WORK, next_work_id)
        work_entity = client.get(work_key, transaction=transaction)
        if not is_unclaimed(work_entity):
          return None
        work_entity['claimed_worker_id'] = worker_id
        work_entity['claimed_worker_start_time'] = get_integer_time()
        transaction.put(work_entity)
    except Exception:
      return None
    return next_work_id