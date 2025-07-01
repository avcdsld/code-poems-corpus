def read_all_from_datastore(self):
    """Reads all work pieces from the datastore."""
    self._work = {}
    client = self._datastore_client
    parent_key = client.key(KIND_WORK_TYPE, self._work_type_entity_id)
    for entity in client.query_fetch(kind=KIND_WORK, ancestor=parent_key):
      work_id = entity.key.flat_path[-1]
      self.work[work_id] = dict(entity)