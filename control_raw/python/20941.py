def histograms_impl(self, tag, run, downsample_to=None):
    """Result of the form `(body, mime_type)`, or `ValueError`.

    At most `downsample_to` events will be returned. If this value is
    `None`, then no downsampling will be performed.
    """
    if self._db_connection_provider:
      # Serve data from the database.
      db = self._db_connection_provider()
      cursor = db.cursor()
      # Prefetch the tag ID matching this run and tag.
      cursor.execute(
          '''
          SELECT
            tag_id
          FROM Tags
          JOIN Runs USING (run_id)
          WHERE
            Runs.run_name = :run
            AND Tags.tag_name = :tag
            AND Tags.plugin_name = :plugin
          ''',
          {'run': run, 'tag': tag, 'plugin': metadata.PLUGIN_NAME})
      row = cursor.fetchone()
      if not row:
        raise ValueError('No histogram tag %r for run %r' % (tag, run))
      (tag_id,) = row
      # Fetch tensor values, optionally with linear-spaced sampling by step.
      # For steps ranging from s_min to s_max and sample size k, this query
      # divides the range into k - 1 equal-sized intervals and returns the
      # lowest step at or above each of the k interval boundaries (which always
      # includes s_min and s_max, and may be fewer than k results if there are
      # intervals where no steps are present). For contiguous steps the results
      # can be formally expressed as the following:
      #   [s_min + math.ceil(i / k * (s_max - s_min)) for i in range(0, k + 1)]
      cursor.execute(
          '''
          SELECT
            MIN(step) AS step,
            computed_time,
            data,
            dtype,
            shape
          FROM Tensors
          INNER JOIN (
            SELECT
              MIN(step) AS min_step,
              MAX(step) AS max_step
            FROM Tensors
            /* Filter out NULL so we can use TensorSeriesStepIndex. */
            WHERE series = :tag_id AND step IS NOT NULL
          )
          /* Ensure we omit reserved rows, which have NULL step values. */
          WHERE series = :tag_id AND step IS NOT NULL
          /* Bucket rows into sample_size linearly spaced buckets, or do
             no sampling if sample_size is NULL. */
          GROUP BY
            IFNULL(:sample_size - 1, max_step - min_step)
            * (step - min_step) / (max_step - min_step)
          ORDER BY step
          ''',
          {'tag_id': tag_id, 'sample_size': downsample_to})
      events = [(computed_time, step, self._get_values(data, dtype, shape))
                for step, computed_time, data, dtype, shape in cursor]
    else:
      # Serve data from events files.
      try:
        tensor_events = self._multiplexer.Tensors(run, tag)
      except KeyError:
        raise ValueError('No histogram tag %r for run %r' % (tag, run))
      if downsample_to is not None and len(tensor_events) > downsample_to:
        rand_indices = random.Random(0).sample(
            six.moves.xrange(len(tensor_events)), downsample_to)
        indices = sorted(rand_indices)
        tensor_events = [tensor_events[i] for i in indices]
      events = [[e.wall_time, e.step, tensor_util.make_ndarray(e.tensor_proto).tolist()]
                for e in tensor_events]
    return (events, 'application/json')