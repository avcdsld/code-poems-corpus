def _ensure_annotations(dashboard):
    '''Explode annotation_tags into annotations.'''
    if 'annotation_tags' not in dashboard:
        return
    tags = dashboard['annotation_tags']
    annotations = {
        'enable': True,
        'list': [],
    }
    for tag in tags:
        annotations['list'].append({
            'datasource': "graphite",
            'enable': False,
            'iconColor': "#C0C6BE",
            'iconSize': 13,
            'lineColor': "rgba(255, 96, 96, 0.592157)",
            'name': tag,
            'showLine': True,
            'tags': tag,
        })
    del dashboard['annotation_tags']
    dashboard['annotations'] = annotations