def _list_nodes(full=False, for_output=False):
    '''
    Helper function to format and parse node data.
    '''
    fetch = True
    page = 1
    ret = {}

    while fetch:
        items = query(method='droplets',
                      command='?page=' + six.text_type(page) + '&per_page=200')
        for node in items['droplets']:
            name = node['name']
            ret[name] = {}
            if full:
                ret[name] = _get_full_output(node, for_output=for_output)
            else:
                public_ips, private_ips = _get_ips(node['networks'])
                ret[name] = {
                    'id': node['id'],
                    'image': node['image']['name'],
                    'name': name,
                    'private_ips': private_ips,
                    'public_ips': public_ips,
                    'size': node['size_slug'],
                    'state': six.text_type(node['status']),
                }

        page += 1
        try:
            fetch = 'next' in items['links']['pages']
        except KeyError:
            fetch = False

    return ret