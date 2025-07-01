def _expand_node(node):
    '''
    Convert the libcloud Node object into something more serializable.
    '''
    ret = {}
    ret.update(node.__dict__)
    try:
        del ret['extra']['boot_disk']
    except Exception:  # pylint: disable=W0703
        pass
    zone = ret['extra']['zone']
    ret['extra']['zone'] = {}
    ret['extra']['zone'].update(zone.__dict__)

    # Remove unserializable GCENodeDriver objects
    if 'driver' in ret:
        del ret['driver']
    if 'driver' in ret['extra']['zone']:
        del ret['extra']['zone']['driver']

    return ret