def list_nodes_full(**kwargs):
    '''
    Return all data on nodes
    '''
    nodes = _query('server/list')
    ret = {}

    for node in nodes:
        name = nodes[node]['label']
        ret[name] = nodes[node].copy()
        ret[name]['id'] = node
        ret[name]['image'] = nodes[node]['os']
        ret[name]['size'] = nodes[node]['VPSPLANID']
        ret[name]['state'] = nodes[node]['status']
        ret[name]['private_ips'] = nodes[node]['internal_ip']
        ret[name]['public_ips'] = nodes[node]['main_ip']

    return ret