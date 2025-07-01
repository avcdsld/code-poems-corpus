def write_all_to_datastore(self):
    """Writes all work pieces into datastore.

    Each work piece is identified by ID. This method writes/updates only those
    work pieces which IDs are stored in this class. For examples, if this class
    has only work pieces with IDs  '1' ... '100' and datastore already contains
    work pieces with IDs '50' ... '200' then this method will create new
    work pieces with IDs '1' ... '49', update work pieces with IDs
    '50' ... '100' and keep unchanged work pieces with IDs '101' ... '200'.
    """
    client = self._datastore_client
    with client.no_transact_batch() as batch:
      parent_key = client.key(KIND_WORK_TYPE, self._work_type_entity_id)
      batch.put(client.entity(parent_key))
      for work_id, work_val in iteritems(self._work):
        entity = client.entity(client.key(KIND_WORK, work_id,
                                          parent=parent_key))
        entity.update(work_val)
        batch.put(entity)