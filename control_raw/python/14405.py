def select(self, field_paths):
        """Create a "select" query with this collection as parent.

        See
        :meth:`~.firestore_v1beta1.query.Query.select` for
        more information on this method.

        Args:
            field_paths (Iterable[str, ...]): An iterable of field paths
                (``.``-delimited list of field names) to use as a projection
                of document fields in the query results.

        Returns:
            ~.firestore_v1beta1.query.Query: A "projected" query.
        """
        query = query_mod.Query(self)
        return query.select(field_paths)