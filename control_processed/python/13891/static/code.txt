def column_spec_path(cls, project, location, dataset, table_spec, column_spec):
        """Return a fully-qualified column_spec string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/datasets/{dataset}/tableSpecs/{table_spec}/columnSpecs/{column_spec}",
            project=project,
            location=location,
            dataset=dataset,
            table_spec=table_spec,
            column_spec=column_spec,
        )