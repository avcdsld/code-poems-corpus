def insert_rows_json(
        self,
        table,
        json_rows,
        row_ids=None,
        skip_invalid_rows=None,
        ignore_unknown_values=None,
        template_suffix=None,
        retry=DEFAULT_RETRY,
    ):
        """Insert rows into a table without applying local type conversions.

        See
        https://cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/insertAll

        table (Union[ \
            :class:`~google.cloud.bigquery.table.Table` \
            :class:`~google.cloud.bigquery.table.TableReference`, \
            str, \
        ]):
            The destination table for the row data, or a reference to it.
        json_rows (Sequence[dict]):
            Row data to be inserted. Keys must match the table schema fields
            and values must be JSON-compatible representations.
        row_ids (Sequence[str]):
            (Optional) Unique ids, one per row being inserted. If omitted,
            unique IDs are created.
        skip_invalid_rows (bool):
            (Optional) Insert all valid rows of a request, even if invalid
            rows exist. The default value is False, which causes the entire
            request to fail if any invalid rows exist.
        ignore_unknown_values (bool):
            (Optional) Accept rows that contain values that do not match the
            schema. The unknown values are ignored. Default is False, which
            treats unknown values as errors.
        template_suffix (str):
            (Optional) treat ``name`` as a template table and provide a suffix.
            BigQuery will create the table ``<name> + <template_suffix>`` based
            on the schema of the template table. See
            https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables
        retry (:class:`google.api_core.retry.Retry`):
            (Optional) How to retry the RPC.

        Returns:
            Sequence[Mappings]:
                One mapping per row with insert errors: the "index" key
                identifies the row, and the "errors" key contains a list of
                the mappings describing one or more problems with the row.
        """
        # Convert table to just a reference because unlike insert_rows,
        # insert_rows_json doesn't need the table schema. It's not doing any
        # type conversions.
        table = _table_arg_to_table_ref(table, default_project=self.project)
        rows_info = []
        data = {"rows": rows_info}

        for index, row in enumerate(json_rows):
            info = {"json": row}
            if row_ids is not None:
                info["insertId"] = row_ids[index]
            else:
                info["insertId"] = str(uuid.uuid4())
            rows_info.append(info)

        if skip_invalid_rows is not None:
            data["skipInvalidRows"] = skip_invalid_rows

        if ignore_unknown_values is not None:
            data["ignoreUnknownValues"] = ignore_unknown_values

        if template_suffix is not None:
            data["templateSuffix"] = template_suffix

        # We can always retry, because every row has an insert ID.
        response = self._call_api(
            retry, method="POST", path="%s/insertAll" % table.path, data=data
        )
        errors = []

        for error in response.get("insertErrors", ()):
            errors.append({"index": int(error["index"]), "errors": error["errors"]})

        return errors