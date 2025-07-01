def list_nodes(**kwargs):
    '''
    Return basic data on nodes
    '''
    ret = {}

    nodes = list_nodes_full()
    for node in nodes:
        ret[node] = {}
        for prop in 'id', 'image', 'size', 'state', 'private_ips', 'public_ips':
            ret[node][prop] = nodes[node][prop]

    return ret