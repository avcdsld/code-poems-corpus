def _session():
    '''
    Create a session to be used when connecting to Zenoss.
    '''

    config = __salt__['config.option']('zenoss')
    session = requests.session()
    session.auth = (config.get('username'), config.get('password'))
    session.verify = False
    session.headers.update({'Content-type': 'application/json; charset=utf-8'})
    return session