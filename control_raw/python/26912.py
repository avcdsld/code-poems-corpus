def port_get_policy(name, sel_type=None, protocol=None, port=None):
    '''
    .. versionadded:: 2019.2.0

    Returns the current entry in the SELinux policy list as a
    dictionary. Returns None if no exact match was found.

    Returned keys are:

    * sel_type (the selinux type)
    * proto (the protocol)
    * port (the port(s) and/or port range(s))

    name
        The protocol and port spec. Can be formatted as ``(tcp|udp)/(port|port-range)``.

    sel_type
        The SELinux Type.

    protocol
        The protocol for the port, ``tcp`` or ``udp``. Required if name is not formatted.

    port
        The port or port range. Required if name is not formatted.

    CLI Example:

    .. code-block:: bash

        salt '*' selinux.port_get_policy tcp/80
        salt '*' selinux.port_get_policy foobar protocol=tcp port=80
    '''
    (protocol, port) = _parse_protocol_port(name, protocol, port)
    re_spacer = '[ ]+'
    re_sel_type = sel_type if sel_type else r'\w+'
    cmd_kwargs = {'spacer': re_spacer,
                  'sel_type': re_sel_type,
                  'protocol': protocol,
                  'port': port, }
    cmd = 'semanage port -l | egrep ' + \
          "'^{sel_type}{spacer}{protocol}{spacer}((.*)*)[ ]{port}($|,)'".format(**cmd_kwargs)
    port_policy = __salt__['cmd.shell'](cmd, ignore_retcode=True)
    if port_policy == '':
        return None

    parts = re.match(r'^(\w+)[ ]+(\w+)[ ]+([\d\-, ]+)', port_policy)
    return {
        'sel_type': parts.group(1).strip(),
        'protocol': parts.group(2).strip(),
        'port': parts.group(3).strip(), }