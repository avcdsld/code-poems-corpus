def request_cert(name, master, ticket, port="5665"):
    '''
    Request CA certificate from master icinga2 node.

    name
        The domain name for which this certificate will be saved

    master
        Icinga2 master node for which this certificate will be saved

    ticket
        Authentication ticket generated on icinga2 master

    port
        Icinga2 port, defaults to 5665
    '''
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': ''}
    cert = "{0}ca.crt".format(get_certs_path())

    # Checking if execution is needed.
    if os.path.isfile(cert):
        ret['comment'] = 'No execution needed. Cert: {0} already exists.'.format(cert)
        return ret
    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'Certificate request from icinga2 master would be executed'
        return ret

    # Executing the command.
    cert_request = __salt__['icinga2.request_cert'](name, master, ticket, port)
    if not cert_request['retcode']:
        ret['comment'] = "Certificate request from icinga2 master executed"
        ret['changes']['cert'] = "Executed. Certificate requested: {0}".format(cert)
        return ret

    ret['comment'] = "FAILED. Certificate requested failed with output: {0}".format(cert_request['stdout'])
    ret['result'] = False
    return ret