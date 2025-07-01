def updateByQuery(self, using=None):
        """
        Return a :class:`~elasticsearch_dsl.UpdateByQuery` object searching over the index
        (or all the indices belonging to this template) and updating Documents that match
        the search criteria.

        For more information, see here:
        https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-update-by-query.html
        """
        return UpdateByQuery(
            using=using or self._using,
            index=self._name,
        )