def _lookup_nslookup(name, rdtype, timeout=None, server=None):
    '''
    Use nslookup to lookup addresses
    :param name: Name of record to search
    :param rdtype: DNS record type
    :param timeout: server response timeout
    :param server: server to query
    :return: [] of records or False if error
    '''
    cmd = 'nslookup -query={0} {1}'.format(rdtype, name)

    if timeout is not None:
        cmd += ' -timeout={0}'.format(int(timeout))
    if server is not None:
        cmd += ' {0}'.format(server)

    cmd = __salt__['cmd.run_all'](cmd, python_shell=False, output_loglevel='quiet')

    if cmd['retcode'] != 0:
        log.warning(
            'nslookup returned (%s): %s',
            cmd['retcode'],
            cmd['stdout'].splitlines()[-1].strip(string.whitespace + ';')
        )
        return False

    lookup_res = iter(cmd['stdout'].splitlines())
    res = []
    try:
        line = next(lookup_res)
        if 'unknown query type' in line:
            raise ValueError('Invalid DNS type {}'.format(rdtype))

        while True:
            if name in line:
                break
            line = next(lookup_res)

        while True:
            line = line.strip()
            if not line or line.startswith('*'):
                break
            elif rdtype != 'CNAME' and 'canonical name' in line:
                name = line.split()[-1][:-1]
                line = next(lookup_res)
                continue
            elif rdtype == 'SOA':
                line = line.split('=')
            elif line.startswith('Name:'):
                line = next(lookup_res)
                line = line.split(':', 1)
            elif line.startswith(name):
                if '=' in line:
                    line = line.split('=', 1)
                else:
                    line = line.split(' ')

            res.append(_data_clean(line[-1]))
            line = next(lookup_res)

    except StopIteration:
        pass

    if rdtype == 'SOA':
        return [' '.join(res[1:])]
    else:
        return res