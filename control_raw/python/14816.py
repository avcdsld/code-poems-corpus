def delete(self, table, keyset):
        """Delete one or more table rows.

        :type table: str
        :param table: Name of the table to be modified.

        :type keyset: :class:`~google.cloud.spanner_v1.keyset.Keyset`
        :param keyset: Keys/ranges identifying rows to delete.
        """
        delete = Mutation.Delete(table=table, key_set=keyset._to_pb())
        self._mutations.append(Mutation(delete=delete))