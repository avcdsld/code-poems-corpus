def migrated(name,
             remote_addr,
             cert,
             key,
             verify_cert,
             src_remote_addr,
             stop_and_start=False,
             src_cert=None,
             src_key=None,
             src_verify_cert=None):
    ''' Ensure a container is migrated to another host

    If the container is running, it either must be shut down
    first (use stop_and_start=True) or criu must be installed
    on the source and destination machines.

    For this operation both certs need to be authenticated,
    use :mod:`lxd.authenticate <salt.states.lxd.authenticate`
    to authenticate your cert(s).

    name :
        The container to migrate

    remote_addr :
        An URL to the destination remote Server

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

    src_remote_addr :
        An URL to the source remote Server

        Examples:
            https://myserver.lan:8443
            /var/lib/mysocket.sock

    stop_and_start:
        Stop before migrating and start after

    src_cert :
        PEM Formatted SSL Zertifikate, if None we copy "cert"

        Examples:
            ~/.config/lxc/client.crt

    src_key :
        PEM Formatted SSL Key, if None we copy "key"

        Examples:
            ~/.config/lxc/client.key

    src_verify_cert :
        Wherever to verify the cert, if None we copy "verify_cert"
    '''
    ret = {
        'name': name,

        'remote_addr': remote_addr,
        'cert': cert,
        'key': key,
        'verify_cert': verify_cert,

        'src_remote_addr': src_remote_addr,
        'src_and_start': stop_and_start,
        'src_cert': src_cert,
        'src_key': src_key,

        'changes': {}
    }

    dest_container = None
    try:
        dest_container = __salt__['lxd.container_get'](
            name, remote_addr, cert, key,
            verify_cert, _raw=True
        )
    except CommandExecutionError as e:
        return _error(ret, six.text_type(e))
    except SaltInvocationError as e:
        # Destination container not found
        pass

    if dest_container is not None:
        return _success(
            ret,
            'Container "{0}" exists on the destination'.format(name)
        )

    if src_verify_cert is None:
        src_verify_cert = verify_cert

    try:
        __salt__['lxd.container_get'](
            name, src_remote_addr, src_cert, src_key, src_verify_cert, _raw=True
        )
    except CommandExecutionError as e:
        return _error(ret, six.text_type(e))
    except SaltInvocationError as e:
        # Container not found
        return _error(ret, 'Source Container "{0}" not found'.format(name))

    if __opts__['test']:
        ret['changes']['migrated'] = (
            'Would migrate the container "{0}" from "{1}" to "{2}"'
        ).format(name, src_remote_addr, remote_addr)
        return _unchanged(ret, ret['changes']['migrated'])

    try:
        __salt__['lxd.container_migrate'](
            name, stop_and_start, remote_addr, cert, key,
            verify_cert, src_remote_addr, src_cert, src_key, src_verify_cert
        )
    except CommandExecutionError as e:
        return _error(ret, six.text_type(e))

    ret['changes']['migrated'] = (
        'Migrated the container "{0}" from "{1}" to "{2}"'
    ).format(name, src_remote_addr, remote_addr)
    return _success(ret, ret['changes']['migrated'])