def create(self, initial_split_keys=[], column_families={}):
        """Creates this table.

        For example:

        .. literalinclude:: snippets_table.py
            :start-after: [START bigtable_create_table]
            :end-before: [END bigtable_create_table]

        .. note::

            A create request returns a
            :class:`._generated.table_pb2.Table` but we don't use
            this response.

        :type initial_split_keys: list
        :param initial_split_keys: (Optional) list of row keys in bytes that
                                   will be used to initially split the table
                                   into several tablets.

        :type column_families: dict
        :param column_failies: (Optional) A map columns to create.  The key is
                               the column_id str and the value is a
                               :class:`GarbageCollectionRule`
        """
        table_client = self._instance._client.table_admin_client
        instance_name = self._instance.name

        families = {
            id: ColumnFamily(id, self, rule).to_pb()
            for (id, rule) in column_families.items()
        }
        table = admin_messages_v2_pb2.Table(column_families=families)

        split = table_admin_messages_v2_pb2.CreateTableRequest.Split
        splits = [split(key=_to_bytes(key)) for key in initial_split_keys]

        table_client.create_table(
            parent=instance_name,
            table_id=self.table_id,
            table=table,
            initial_splits=splits,
        )