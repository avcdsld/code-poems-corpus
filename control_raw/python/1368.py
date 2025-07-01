def _create_table_setup(self):
        """
        Return a list of SQL statements that creates a table reflecting the
        structure of a DataFrame.  The first entry will be a CREATE TABLE
        statement while the rest will be CREATE INDEX statements.
        """
        column_names_and_types = self._get_column_names_and_types(
            self._sql_type_name
        )

        pat = re.compile(r'\s+')
        column_names = [col_name for col_name, _, _ in column_names_and_types]
        if any(map(pat.search, column_names)):
            warnings.warn(_SAFE_NAMES_WARNING, stacklevel=6)

        escape = _get_valid_sqlite_name

        create_tbl_stmts = [escape(cname) + ' ' + ctype
                            for cname, ctype, _ in column_names_and_types]

        if self.keys is not None and len(self.keys):
            if not is_list_like(self.keys):
                keys = [self.keys]
            else:
                keys = self.keys
            cnames_br = ", ".join(escape(c) for c in keys)
            create_tbl_stmts.append(
                "CONSTRAINT {tbl}_pk PRIMARY KEY ({cnames_br})".format(
                    tbl=self.name, cnames_br=cnames_br))

        create_stmts = ["CREATE TABLE " + escape(self.name) + " (\n" +
                        ',\n  '.join(create_tbl_stmts) + "\n)"]

        ix_cols = [cname for cname, _, is_index in column_names_and_types
                   if is_index]
        if len(ix_cols):
            cnames = "_".join(ix_cols)
            cnames_br = ",".join(escape(c) for c in ix_cols)
            create_stmts.append(
                "CREATE INDEX " + escape("ix_" + self.name + "_" + cnames) +
                "ON " + escape(self.name) + " (" + cnames_br + ")")

        return create_stmts