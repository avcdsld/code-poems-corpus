def _get_nics(vm_):
    '''
    Create network interfaces on appropriate LANs as defined in cloud profile.
    '''
    nics = []
    if 'public_lan' in vm_:
        firewall_rules = []
        # Set LAN to public if it already exists, otherwise create a new
        # public LAN.
        if 'public_firewall_rules' in vm_:
            firewall_rules = _get_firewall_rules(vm_['public_firewall_rules'])
        nic = NIC(lan=set_public_lan(int(vm_['public_lan'])),
                  name='public',
                  firewall_rules=firewall_rules)
        if 'public_ips' in vm_:
            nic.ips = _get_ip_addresses(vm_['public_ips'])
        nics.append(nic)

    if 'private_lan' in vm_:
        firewall_rules = []
        if 'private_firewall_rules' in vm_:
            firewall_rules = _get_firewall_rules(vm_['private_firewall_rules'])
        nic = NIC(lan=int(vm_['private_lan']),
                  name='private',
                  firewall_rules=firewall_rules)
        if 'private_ips' in vm_:
            nic.ips = _get_ip_addresses(vm_['private_ips'])
        if 'nat' in vm_ and 'private_ips' not in vm_:
            nic.nat = vm_['nat']
        nics.append(nic)
    return nics