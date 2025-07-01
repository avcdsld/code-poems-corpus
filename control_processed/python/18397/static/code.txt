def issue_tags(issue):
    """Returns list of tags for this issue."""
    labels = issue.get('labels', [])
    return [label['name'].replace('tag: ', '') for label in labels if label['name'].startswith('tag: ')]