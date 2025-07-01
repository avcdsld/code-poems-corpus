def column_families(self):
        """List[:class:`~.external_config.BigtableColumnFamily`]: List of
        column families to expose in the table schema along with their types.

        See
        https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs#configuration.query.tableDefinitions.(key).bigtableOptions.columnFamilies
        https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#externalDataConfiguration.bigtableOptions.columnFamilies
        """
        prop = self._properties.get("columnFamilies", [])
        return [BigtableColumnFamily.from_api_repr(cf) for cf in prop]