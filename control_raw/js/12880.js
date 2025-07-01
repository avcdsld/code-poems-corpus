function buildCountCommand(collectionOrCursor, query, options) {
  const skip = options.skip;
  const limit = options.limit;
  let hint = options.hint;
  const maxTimeMS = options.maxTimeMS;
  query = query || {};

  // Final query
  const cmd = {
    count: options.collectionName,
    query: query
  };

  // check if collectionOrCursor is a cursor by using cursor.s.numberOfRetries
  if (collectionOrCursor.s.numberOfRetries) {
    if (collectionOrCursor.s.options.hint) {
      hint = collectionOrCursor.s.options.hint;
    } else if (collectionOrCursor.s.cmd.hint) {
      hint = collectionOrCursor.s.cmd.hint;
    }
    decorateWithCollation(cmd, collectionOrCursor, collectionOrCursor.s.cmd);
  } else {
    decorateWithCollation(cmd, collectionOrCursor, options);
  }

  // Add limit, skip and maxTimeMS if defined
  if (typeof skip === 'number') cmd.skip = skip;
  if (typeof limit === 'number') cmd.limit = limit;
  if (typeof maxTimeMS === 'number') cmd.maxTimeMS = maxTimeMS;
  if (hint) cmd.hint = hint;

  // Do we have a readConcern specified
  decorateWithReadConcern(cmd, collectionOrCursor);

  return cmd;
}