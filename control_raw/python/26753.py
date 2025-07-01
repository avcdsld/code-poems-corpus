def avail_sizes(call=None):
    '''
    Return a dict of all available VM sizes on the cloud provider with
    relevant data. This data is provided in three dicts.
    '''
    if call == 'action':
        raise SaltCloudSystemExit(
            'The avail_sizes function must be called with '
            '-f or --function, or with the --list-sizes option'
        )

    ret = {
        'block devices': {},
        'memory': {},
        'processors': {},
    }
    conn = get_conn()
    response = conn.getCreateObjectOptions()
    for device in response['blockDevices']:
        #return device['template']['blockDevices']
        ret['block devices'][device['itemPrice']['item']['description']] = {
            'name': device['itemPrice']['item']['description'],
            'capacity':
                device['template']['blockDevices'][0]['diskImage']['capacity'],
        }
    for memory in response['memory']:
        ret['memory'][memory['itemPrice']['item']['description']] = {
            'name': memory['itemPrice']['item']['description'],
            'maxMemory': memory['template']['maxMemory'],
        }
    for processors in response['processors']:
        ret['processors'][processors['itemPrice']['item']['description']] = {
            'name': processors['itemPrice']['item']['description'],
            'start cpus': processors['template']['startCpus'],
        }
    return ret