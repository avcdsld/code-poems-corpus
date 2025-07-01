def list_experiments(project_path, sort, output, filter_op, columns):
    """Lists experiments in the directory subtree."""
    if columns:
        columns = columns.split(",")
    commands.list_experiments(project_path, sort, output, filter_op, columns)