def absent(name,
           stop=False,
           remote_addr=None,
           cert=None,
           key=None,
           verify_cert=True):
    '''
    Ensure a LXD container is not present, destroying it if present

    name :
        The name of the container to destroy

    stop :
        stop before destroying
        default: false

    remote_addr :
        An URL to a remote Server, you also have to give cert and key if you
        provide remote_addr!

        Examples:
            https://myserver.lan:8443
            /var/lib/mysocket.sock

    cert :
        PEM Formatted SSL Zertifikate.

        Examples:
            ~/.config/lxc/client.crt

    key :
        PEM Formatted SSL Key.

        Examples:
            ~/.config/lxc/client.key

    verify_cert : True
        Wherever to verify the cert, this is by default True
        but in the most cases you want to set it off as LXD
        normaly uses self-signed certificates.
    '''
    ret = {
        'name': name,
        'stop': stop,

        'remote_addr': remote_addr,
        'cert': cert,
        'key': key,
        'verify_cert': verify_cert,

        'changes': {}
    }

    try:
        container = __salt__['lxd.container_get'](
            name, remote_addr, cert, key, verify_cert, _raw=True
        )
    except CommandExecutionError as e:
        return _error(ret, six.text_type(e))
    except SaltInvocationError as e:
        # Container not found
        return _success(ret, 'Container "{0}" not found.'.format(name))

    if __opts__['test']:
        ret['changes'] = {
            'removed':
            'Container "{0}" would get deleted.'.format(name)
        }
        return _unchanged(ret, ret['changes']['removed'])

    if stop and container.status_code == CONTAINER_STATUS_RUNNING:
        container.stop(wait=True)

    container.delete(wait=True)

    ret['changes']['deleted'] = \
        'Container "{0}" has been deleted.'.format(name)
    return _success(ret, ret['changes']['deleted'])