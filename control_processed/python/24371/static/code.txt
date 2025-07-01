def shutdown(opts):
    '''
    Closes connection with the device.
    '''
    try:
        if not NETWORK_DEVICE.get('UP', False):
            raise Exception('not connected!')
        NETWORK_DEVICE.get('DRIVER').close()
    except Exception as error:
        port = NETWORK_DEVICE.get('OPTIONAL_ARGS', {}).get('port')
        log.error(
            'Cannot close connection with %s%s! Please check error: %s',
            NETWORK_DEVICE.get('HOSTNAME', '[unknown hostname]'),
            ':{0}'.format(port) if port else '',
            error
        )

    return True