def ddl_target_table(self):
        """Optional[TableReference]: Return the DDL target table, present
            for CREATE/DROP TABLE/VIEW queries.

        See:
        https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs#statistics.query.ddlTargetTable
        """
        prop = self._job_statistics().get("ddlTargetTable")
        if prop is not None:
            prop = TableReference.from_api_repr(prop)
        return prop