def list_loadbalancers(call=None):
    '''
    Return a list of the loadbalancers that are on the provider
    '''
    if call == 'action':
        raise SaltCloudSystemExit(
            'The avail_images function must be called with '
            '-f or --function, or with the --list-loadbalancers option'
        )

    ret = {}
    conn = get_conn()
    datacenter = get_datacenter(conn)

    for item in conn.list_loadbalancers(datacenter['id'])['items']:
        lb = {'id': item['id']}
        lb.update(item['properties'])
        ret[lb['name']] = lb

    return ret