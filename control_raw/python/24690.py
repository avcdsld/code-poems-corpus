def get_vmconfig(vmid, node=None, node_type='openvz'):
    '''
    Get VM configuration
    '''
    if node is None:
        # We need to figure out which node this VM is on.
        for host_name, host_details in six.iteritems(avail_locations()):
            for item in query('get', 'nodes/{0}/{1}'.format(host_name, node_type)):
                if item['vmid'] == vmid:
                    node = host_name

    # If we reached this point, we have all the information we need
    data = query('get', 'nodes/{0}/{1}/{2}/config'.format(node, node_type, vmid))

    return data