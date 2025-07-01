def list_bindings(site):
    '''
    Get all configured IIS bindings for the specified site.

    Args:
        site (str): The name if the IIS Site

    Returns:
        dict: A dictionary of the binding names and properties.

    CLI Example:

    .. code-block:: bash

        salt '*' win_iis.list_bindings site
    '''
    ret = dict()
    sites = list_sites()

    if site not in sites:
        log.warning('Site not found: %s', site)
        return ret

    ret = sites[site]['bindings']

    if not ret:
        log.warning('No bindings found for site: %s', site)

    return ret