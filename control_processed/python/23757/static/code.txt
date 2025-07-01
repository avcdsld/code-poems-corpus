def _parse_interfaces(interface_files=None):
    '''
    Parse /etc/network/interfaces and return current configured interfaces
    '''
    if interface_files is None:
        interface_files = []
        # Add this later.
        if os.path.exists(_DEB_NETWORK_DIR):
            interface_files += ['{0}/{1}'.format(_DEB_NETWORK_DIR, dir) for dir in os.listdir(_DEB_NETWORK_DIR)]

        if os.path.isfile(_DEB_NETWORK_FILE):
            interface_files.insert(0, _DEB_NETWORK_FILE)

    adapters = salt.utils.odict.OrderedDict()
    method = -1

    for interface_file in interface_files:
        with salt.utils.files.fopen(interface_file) as interfaces:
            # This ensures iface_dict exists, but does not ensure we're not reading a new interface.
            iface_dict = {}
            for line in interfaces:
                line = salt.utils.stringutils.to_unicode(line)
                # Identify the clauses by the first word of each line.
                # Go to the next line if the current line is a comment
                # or all spaces.
                if line.lstrip().startswith('#') or line.isspace():
                    continue
                # Parse the iface clause
                if line.startswith('iface'):
                    sline = line.split()

                    if len(sline) != 4:
                        msg = 'Interface file malformed: {0}.'
                        msg = msg.format(sline)
                        log.error(msg)
                        raise AttributeError(msg)

                    iface_name = sline[1]
                    addrfam = sline[2]
                    method = sline[3]

                    # Create item in dict, if not already there
                    if iface_name not in adapters:
                        adapters[iface_name] = salt.utils.odict.OrderedDict()

                    # Create item in dict, if not already there
                    if 'data' not in adapters[iface_name]:
                        adapters[iface_name]['data'] = salt.utils.odict.OrderedDict()

                    if addrfam not in adapters[iface_name]['data']:
                        adapters[iface_name]['data'][addrfam] = salt.utils.odict.OrderedDict()

                    iface_dict = adapters[iface_name]['data'][addrfam]

                    iface_dict['addrfam'] = addrfam
                    iface_dict['proto'] = method
                    iface_dict['filename'] = interface_file

                # Parse the detail clauses.
                elif line[0].isspace():
                    sline = line.split()

                    # conf file attr: dns-nameservers
                    # salt states.network attr: dns

                    attr, valuestr = line.rstrip().split(None, 1)
                    if _attrmaps_contain_attr(attr):
                        if '-' in attr:
                            attrname = attr.replace('-', '_')
                        else:
                            attrname = attr
                        (valid, value, errmsg) = _validate_interface_option(
                            attr, valuestr, addrfam)
                        if attrname == 'address' and 'address' in iface_dict:
                            if 'addresses' not in iface_dict:
                                iface_dict['addresses'] = []
                            iface_dict['addresses'].append(value)
                        else:
                            iface_dict[attrname] = value

                    elif attr in _REV_ETHTOOL_CONFIG_OPTS:
                        if 'ethtool' not in iface_dict:
                            iface_dict['ethtool'] = salt.utils.odict.OrderedDict()
                        iface_dict['ethtool'][attr] = valuestr

                    elif attr.startswith('bond'):
                        opt = re.split(r'[_-]', attr, maxsplit=1)[1]
                        if 'bonding' not in iface_dict:
                            iface_dict['bonding'] = salt.utils.odict.OrderedDict()
                        iface_dict['bonding'][opt] = valuestr

                    elif attr.startswith('bridge'):
                        opt = re.split(r'[_-]', attr, maxsplit=1)[1]
                        if 'bridging' not in iface_dict:
                            iface_dict['bridging'] = salt.utils.odict.OrderedDict()
                        iface_dict['bridging'][opt] = valuestr

                    elif attr in ['up', 'pre-up', 'post-up',
                                  'down', 'pre-down', 'post-down']:
                        cmd = valuestr
                        cmd_key = '{0}_cmds'.format(re.sub('-', '_', attr))
                        if cmd_key not in iface_dict:
                            iface_dict[cmd_key] = []
                        iface_dict[cmd_key].append(cmd)

                elif line.startswith('auto'):
                    for word in line.split()[1:]:
                        if word not in adapters:
                            adapters[word] = salt.utils.odict.OrderedDict()
                        adapters[word]['enabled'] = True

                elif line.startswith('allow-hotplug'):
                    for word in line.split()[1:]:
                        if word not in adapters:
                            adapters[word] = salt.utils.odict.OrderedDict()
                        adapters[word]['hotplug'] = True

                elif line.startswith('source'):
                    if 'source' not in adapters:
                        adapters['source'] = salt.utils.odict.OrderedDict()

                    # Create item in dict, if not already there
                    if 'data' not in adapters['source']:
                        adapters['source']['data'] = salt.utils.odict.OrderedDict()
                        adapters['source']['data']['sources'] = []
                    adapters['source']['data']['sources'].append(line.split()[1])

    # Return a sorted list of the keys for bond, bridge and ethtool options to
    # ensure a consistent order
    for iface_name in adapters:
        if iface_name == 'source':
            continue
        if 'data' not in adapters[iface_name]:
            msg = 'Interface file malformed for interface: {0}.'.format(iface_name)
            log.error(msg)
            adapters.pop(iface_name)
            continue
        for opt in ['ethtool', 'bonding', 'bridging']:
            for inet in ['inet', 'inet6']:
                if inet in adapters[iface_name]['data']:
                    if opt in adapters[iface_name]['data'][inet]:
                        opt_keys = sorted(adapters[iface_name]['data'][inet][opt].keys())
                        adapters[iface_name]['data'][inet][opt + '_keys'] = opt_keys

    return adapters