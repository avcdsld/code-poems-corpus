def remove_cert_binding(name, site, hostheader='', ipaddress='*', port=443):
    '''
    Remove a certificate from an IIS binding.

    .. note:

        This function only removes the certificate from the web binding. It does
        not remove the web binding itself.

    :param str name: The thumbprint of the certificate.
    :param str site: The IIS site name.
    :param str hostheader: The host header of the binding.
    :param str ipaddress: The IP address of the binding.
    :param str port: The TCP port of the binding.

    Example of usage with only the required arguments:

    .. code-block:: yaml

        site0-cert-binding-remove:
            win_iis.remove_cert_binding:
                - name: 9988776655443322111000AAABBBCCCDDDEEEFFF
                - site: site0

    Example of usage specifying all available arguments:

    .. code-block:: yaml

        site0-cert-binding-remove:
            win_iis.remove_cert_binding:
                - name: 9988776655443322111000AAABBBCCCDDDEEEFFF
                - site: site0
                - hostheader: site0.local
                - ipaddress: 192.168.1.199
                - port: 443

    .. versionadded:: 2016.11.0
    '''
    ret = {'name': name,
           'changes': {},
           'comment': str(),
           'result': None}

    binding_info = _get_binding_info(hostheader, ipaddress, port)
    current_cert_bindings = __salt__['win_iis.list_cert_bindings'](site)

    if binding_info not in current_cert_bindings:
        ret['comment'] = 'Certificate binding has already been removed: {0}'.format(name)
        ret['result'] = True
    elif __opts__['test']:
        ret['comment'] = 'Certificate binding will be removed: {0}'.format(name)
        ret['changes'] = {'old': name,
                          'new': None}
    else:
        current_name = current_cert_bindings[binding_info]['certificatehash']

        if name == current_name:
            ret['comment'] = 'Removed certificate binding: {0}'.format(name)
            ret['changes'] = {'old': name,
                              'new': None}
            ret['result'] = __salt__['win_iis.remove_cert_binding'](name, site, hostheader,
                                                                    ipaddress, port)
    return ret