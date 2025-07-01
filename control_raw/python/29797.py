def is_escaped(url):
    '''
    test whether `url` is escaped with `|`
    '''
    scheme = urlparse(url).scheme
    if not scheme:
        return url.startswith('|')
    elif scheme == 'salt':
        path, saltenv = parse(url)
        if salt.utils.platform.is_windows() and '|' in url:
            return path.startswith('_')
        else:
            return path.startswith('|')
    else:
        return False