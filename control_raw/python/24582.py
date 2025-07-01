def _get_request_mode_info(interface):
    '''
    return requestmode for given interface
    '''
    settings = _load_config(interface, ['linklocalenabled', 'dhcpenabled'], -1)
    link_local_enabled = int(settings['linklocalenabled'])
    dhcp_enabled = int(settings['dhcpenabled'])

    if dhcp_enabled == 1:
        return 'dhcp_linklocal' if link_local_enabled == 1 else 'dhcp_only'
    else:
        if link_local_enabled == 1:
            return 'linklocal_only'
        if link_local_enabled == 0:
            return 'static'

    # some versions of nirtcfg don't set the dhcpenabled/linklocalenabled variables
    # when selecting "DHCP or Link Local" from MAX, so return it by default to avoid
    # having the requestmode "None" because none of the conditions above matched.
    return 'dhcp_linklocal'