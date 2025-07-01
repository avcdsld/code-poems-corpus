def present(name, ip, clean=False):  # pylint: disable=C0103
    '''
    Ensures that the named host is present with the given ip

    name
        The host to assign an ip to

    ip
        The ip addr(s) to apply to the host. Can be a single IP or a list of IP
        addresses.

    clean : False
        Remove any entries which don't match those configured in the ``ip``
        option.

        .. versionadded:: 2018.3.4
    '''
    ret = {'name': name,
           'changes': {},
           'result': None if __opts__['test'] else True,
           'comment': ''}

    if not isinstance(ip, list):
        ip = [ip]

    all_hosts = __salt__['hosts.list_hosts']()
    comments = []
    to_add = set()
    to_remove = set()

    # First check for IPs not currently in the hosts file
    to_add.update([(addr, name) for addr in ip if addr not in all_hosts])

    # Now sweep through the hosts file and look for entries matching either the
    # IP address(es) or hostname.
    for addr, aliases in six.iteritems(all_hosts):
        if addr not in ip:
            if name in aliases:
                # Found match for hostname, but the corresponding IP is not in
                # our list, so we need to remove it.
                if clean:
                    to_remove.add((addr, name))
                else:
                    ret.setdefault('warnings', []).append(
                        'Host {0} present for IP address {1}. To get rid of '
                        'this warning, either run this state with \'clean\' '
                        'set to True to remove {0} from {1}, or add {1} to '
                        'the \'ip\' argument.'.format(name, addr)
                    )
        else:
            if name in aliases:
                # No changes needed for this IP address and hostname
                comments.append(
                    'Host {0} ({1}) already present'.format(name, addr)
                )
            else:
                # IP address listed in hosts file, but hostname is not present.
                # We will need to add it.
                if salt.utils.validate.net.ip_addr(addr):
                    to_add.add((addr, name))
                else:
                    ret['result'] = False
                    comments.append(
                        'Invalid IP Address for {0} ({1})'.format(name, addr)
                    )

    for addr, name in to_add:
        if __opts__['test']:
            comments.append(
                'Host {0} ({1}) would be added'.format(name, addr)
            )
        else:
            if __salt__['hosts.add_host'](addr, name):
                comments.append('Added host {0} ({1})'.format(name, addr))
            else:
                ret['result'] = False
                comments.append('Failed to add host {0} ({1})'.format(name, addr))
                continue
        ret['changes'].setdefault('added', {}).setdefault(addr, []).append(name)

    for addr, name in to_remove:
        if __opts__['test']:
            comments.append(
                'Host {0} ({1}) would be removed'.format(name, addr)
            )
        else:
            if __salt__['hosts.rm_host'](addr, name):
                comments.append('Removed host {0} ({1})'.format(name, addr))
            else:
                ret['result'] = False
                comments.append('Failed to remove host {0} ({1})'.format(name, addr))
                continue
        ret['changes'].setdefault('removed', {}).setdefault(addr, []).append(name)

    ret['comment'] = '\n'.join(comments)
    return ret