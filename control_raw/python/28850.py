def lldp(device=None,
         interface=None,
         title=None,
         pattern=None,
         chassis=None,
         display=_DEFAULT_DISPLAY):
    '''
    Search in the LLDP neighbors, using the following mine functions:

    - net.lldp

    Optional arguments:

    device
        Return interface data from a certain device only.

    interface
        Return data selecting by interface name.

    pattern
        Return LLDP neighbors that have contain this pattern in one of the following fields:

        - Remote Port ID
        - Remote Port Description
        - Remote System Name
        - Remote System Description

    chassis
        Search using a specific Chassis ID.

    display: ``True``
        Display on the screen or return structured object? Default: ``True`` (return on the CLI).

    display: ``True``
        Display on the screen or return structured object? Default: ``True`` (return on the CLI).

    title
        Display a custom title for the table.

    CLI Example:

    .. code-block:: bash

        $ sudo salt-run net.lldp pattern=Ethernet1/48

    Output Example:

    .. code-block:: text

        Pattern "Ethernet1/48" found in one of the following LLDP details
        _________________________________________________________________________________________________________________________________________________________________________________________
        |    Device    | Interface | Parent Interface | Remote Chassis ID | Remote Port ID | Remote Port Description |   Remote System Name   |            Remote System Description            |
        _________________________________________________________________________________________________________________________________________________________________________________________
        | edge01.bjm01 |  xe-2/3/4 |       ae0        | 8C:60:4F:3B:52:19 |                |       Ethernet1/48      | edge05.bjm01.dummy.net |   Cisco NX-OS(tm) n6000, Software (n6000-uk9),  |
        |              |           |                  |                   |                |                         |                        | Version 7.3(0)N7(5), RELEASE SOFTWARE Copyright |
        |              |           |                  |                   |                |                         |                        |  (c) 2002-2012 by Cisco Systems, Inc. Compiled  |
        |              |           |                  |                   |                |                         |                        |                2/17/2016 22:00:00               |
        _________________________________________________________________________________________________________________________________________________________________________________________
        | edge01.flw01 |  xe-1/2/3 |       ae0        | 8C:60:4F:1A:B4:22 |                |       Ethernet1/48      | edge05.flw01.dummy.net |   Cisco NX-OS(tm) n6000, Software (n6000-uk9),  |
        |              |           |                  |                   |                |                         |                        | Version 7.3(0)N7(5), RELEASE SOFTWARE Copyright |
        |              |           |                  |                   |                |                         |                        |  (c) 2002-2012 by Cisco Systems, Inc. Compiled  |
        |              |           |                  |                   |                |                         |                        |                2/17/2016 22:00:00               |
        _________________________________________________________________________________________________________________________________________________________________________________________
        | edge01.oua01 |  xe-0/1/2 |       ae1        | 8C:60:4F:51:A4:22 |                |       Ethernet1/48      | edge05.oua01.dummy.net |   Cisco NX-OS(tm) n6000, Software (n6000-uk9),  |
        |              |           |                  |                   |                |                         |                        | Version 7.3(0)N7(5), RELEASE SOFTWARE Copyright |
        |              |           |                  |                   |                |                         |                        |  (c) 2002-2012 by Cisco Systems, Inc. Compiled  |
        |              |           |                  |                   |                |                         |                        |                2/17/2016 22:00:00               |
        _________________________________________________________________________________________________________________________________________________________________________________________
    '''
    all_lldp = _get_mine('net.lldp')

    labels = {
        'device': 'Device',
        'interface': 'Interface',
        'parent_interface': 'Parent Interface',
        'remote_chassis_id': 'Remote Chassis ID',
        'remote_port_id': 'Remote Port ID',
        'remote_port_desc': 'Remote Port Description',
        'remote_system_name': 'Remote System Name',
        'remote_system_desc': 'Remote System Description'
    }
    rows = []

    if pattern:
        title = 'Pattern "{0}" found in one of the following LLDP details'.format(pattern)
    if not title:
        title = 'LLDP Neighbors'
        if interface:
            title += ' for interface {0}'.format(interface)
        else:
            title += ' for all interfaces'
        if device:
            title += ' on device {0}'.format(device)
        if chassis:
            title += ' having Chassis ID {0}'.format(chassis)

    if device:
        all_lldp = {device: all_lldp.get(device)}

    for device, device_lldp in six.iteritems(all_lldp):
        if not device_lldp:
            continue
        if not device_lldp.get('result', False):
            continue
        lldp_interfaces = device_lldp.get('out', {})
        if interface:
            lldp_interfaces = {interface: lldp_interfaces.get(interface, [])}
        for intrf, interface_lldp in six.iteritems(lldp_interfaces):
            if not interface_lldp:
                continue
            for lldp_row in interface_lldp:
                rsn = (lldp_row.get('remote_system_name', '') or '')
                rpi = (lldp_row.get('remote_port_id', '') or '')
                rsd = (lldp_row.get('remote_system_description', '') or '')
                rpd = (lldp_row.get('remote_port_description', '') or '')
                rci = (lldp_row.get('remote_chassis_id', '') or '')
                if pattern:
                    ptl = pattern.lower()
                    if not((ptl in rsn.lower()) or (ptl in rsd.lower()) or
                           (ptl in rpd.lower()) or (ptl in rci.lower())):
                        # nothing matched, let's move on
                        continue
                if chassis:
                    if (napalm_helpers.convert(napalm_helpers.mac, rci) !=
                       napalm_helpers.convert(napalm_helpers.mac, chassis)):
                        continue
                rows.append({
                    'device': device,
                    'interface': intrf,
                    'parent_interface': (lldp_row.get('parent_interface', '') or ''),
                    'remote_chassis_id': napalm_helpers.convert(napalm_helpers.mac, rci),
                    'remote_port_id': rpi,
                    'remote_port_descr': rpd,
                    'remote_system_name': rsn,
                    'remote_system_descr': rsd
                })

    return _display_runner(rows, labels, title, display=display)