def port_add_policy(name, sel_type=None, protocol=None, port=None, sel_range=None):
    '''
    .. versionadded:: 2019.2.0

    Adds the SELinux policy for a given protocol and port.

    Returns the result of the call to semanage.

    name
        The protocol and port spec. Can be formatted as ``(tcp|udp)/(port|port-range)``.

    sel_type
        The SELinux Type. Required.

    protocol
        The protocol for the port, ``tcp`` or ``udp``. Required if name is not formatted.

    port
        The port or port range. Required if name is not formatted.

    sel_range
        The SELinux MLS/MCS Security Range.

    CLI Example:

    .. code-block:: bash

        salt '*' selinux.port_add_policy add tcp/8080 http_port_t
        salt '*' selinux.port_add_policy add foobar http_port_t protocol=tcp port=8091
    '''
    return _port_add_or_delete_policy('add', name, sel_type, protocol, port, sel_range)