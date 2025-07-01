def _import_status(data, item, repo_name, repo_tag):
    '''
    Process a status update from docker import, updating the data structure
    '''
    status = item['status']
    try:
        if 'Downloading from' in status:
            return
        elif all(x in string.hexdigits for x in status):
            # Status is an image ID
            data['Image'] = '{0}:{1}'.format(repo_name, repo_tag)
            data['Id'] = status
    except (AttributeError, TypeError):
        pass