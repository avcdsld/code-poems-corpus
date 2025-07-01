def order_by(self, field_path, **kwargs):
        """Create an "order by" query with this collection as parent.

        See
        :meth:`~.firestore_v1beta1.query.Query.order_by` for
        more information on this method.

        Args:
            field_path (str): A field path (``.``-delimited list of
                field names) on which to order the query results.
            kwargs (Dict[str, Any]): The keyword arguments to pass along
                to the query. The only supported keyword is ``direction``,
                see :meth:`~.firestore_v1beta1.query.Query.order_by` for
                more information.

        Returns:
            ~.firestore_v1beta1.query.Query: An "order by" query.
        """
        query = query_mod.Query(self)
        return query.order_by(field_path, **kwargs)