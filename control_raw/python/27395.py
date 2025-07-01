def _query(action=None,
           routing_key=None,
           args=None,
           method='GET',
           header_dict=None,
           data=None):
    '''
    Make a web call to VictorOps
    '''
    api_key = __salt__['config.get']('victorops.api_key') or \
        __salt__['config.get']('victorops:api_key')

    path = 'https://alert.victorops.com/integrations/generic/20131114/'

    if action:
        path += '{0}/'.format(action)

    if api_key:
        path += '{0}/'.format(api_key)

    if routing_key:
        path += routing_key

    log.debug('VictorOps URL: %s', path)

    if not isinstance(args, dict):
        args = {}

    if header_dict is None:
        header_dict = {'Content-type': 'application/json'}

    if method != 'POST':
        header_dict['Accept'] = 'application/json'

    decode = True
    if method == 'DELETE':
        decode = False

    result = salt.utils.http.query(
        path,
        method,
        params=args,
        data=data,
        header_dict=header_dict,
        decode=decode,
        decode_type='json',
        text=True,
        status=True,
        cookies=True,
        persist_session=True,
        opts=__opts__,
    )
    if 'error' in result:
        log.error(result['error'])
        return [result['status'], result['error']]

    return [result['status'], result.get('dict', {})]