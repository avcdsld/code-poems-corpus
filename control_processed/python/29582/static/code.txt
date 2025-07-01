def wollist(maclist, bcast='255.255.255.255', destport=9):
    '''
    Send a "Magic Packet" to wake up a list of Minions.
    This list must contain one MAC hardware address per line

    CLI Example:

    .. code-block:: bash

        salt-run network.wollist '/path/to/maclist'
        salt-run network.wollist '/path/to/maclist' 255.255.255.255 7
        salt-run network.wollist '/path/to/maclist' 255.255.255.255 7
    '''
    ret = []
    try:
        with salt.utils.files.fopen(maclist, 'r') as ifile:
            for mac in ifile:
                mac = salt.utils.stringutils.to_unicode(mac).strip()
                wol(mac, bcast, destport)
                print('Waking up {0}'.format(mac))
                ret.append(mac)
    except Exception as err:
        __jid_event__.fire_event({'error': 'Failed to open the MAC file. Error: {0}'.format(err)}, 'progress')
        return []
    return ret