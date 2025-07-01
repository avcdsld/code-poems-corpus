def _property_parse_cmd(cmd, alias=None):
    '''
    Parse output of zpool/zfs get command
    '''
    if not alias:
        alias = {}
    properties = {}

    # NOTE: append get to command
    if cmd[-3:] != 'get':
        cmd += ' get'

    # NOTE: parse output
    prop_hdr = []
    for prop_data in _exec(cmd=cmd)['stderr'].split('\n'):
        # NOTE: make the line data more managable
        prop_data = prop_data.lower().split()

        # NOTE: skip empty lines
        if not prop_data:
            continue
        # NOTE: parse header
        elif prop_data[0] == 'property':
            prop_hdr = prop_data
            continue
        # NOTE: skip lines after data
        elif not prop_hdr or prop_data[1] not in ['no', 'yes']:
            continue

        # NOTE: create property dict
        prop = _property_create_dict(prop_hdr, prop_data)

        # NOTE: add property to dict
        properties[prop['name']] = prop
        if prop['name'] in alias:
            properties[alias[prop['name']]] = prop

        # NOTE: cleanup some duplicate data
        del prop['name']
    return properties