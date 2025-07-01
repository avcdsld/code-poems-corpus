def _apply_network_adapter_config(key, network_name, adapter_type, switch_type,
                                  network_adapter_label=None, operation='add',
                                  connectable=None, mac=None, parent=None):
    '''
    Returns a vim.vm.device.VirtualDeviceSpec object specifying to add/edit a
    network device

    network_adapter_label
        Network adapter label

    key
        Unique key for device creation

    network_name
        Network or port group name

    adapter_type
        Type of the adapter eg. vmxnet3

    switch_type
        Type of the switch: standard or distributed

    operation
        Type of operation: add or edit

    connectable
        Dictionary with the device connection properties

    mac
        MAC address of the network adapter

    parent
        Parent object reference
    '''
    adapter_type.strip().lower()
    switch_type.strip().lower()
    log.trace('Configuring virtual machine network adapter '
              'network_adapter_label=%s network_name=%s '
              'adapter_type=%s switch_type=%s mac=%s',
              network_adapter_label, network_name, adapter_type,
              switch_type, mac)
    network_spec = vim.vm.device.VirtualDeviceSpec()
    network_spec.device = _create_adapter_type(
        network_spec.device,
        adapter_type,
        network_adapter_label=network_adapter_label)
    network_spec.device.deviceInfo = vim.Description()
    if operation == 'add':
        network_spec.operation = \
            vim.vm.device.VirtualDeviceSpec.Operation.add
    elif operation == 'edit':
        network_spec.operation = \
            vim.vm.device.VirtualDeviceSpec.Operation.edit
    if switch_type and network_name:
        network_spec.device.backing = _create_network_backing(network_name,
                                                              switch_type,
                                                              parent)
        network_spec.device.deviceInfo.summary = network_name
    if key:
        # random negative integer for creations, concrete device key
        # for updates
        network_spec.device.key = key
    if network_adapter_label:
        network_spec.device.deviceInfo.label = network_adapter_label
    if mac:
        network_spec.device.macAddress = mac
        network_spec.device.addressType = 'Manual'
    network_spec.device.wakeOnLanEnabled = True
    if connectable:
        network_spec.device.connectable = \
            vim.vm.device.VirtualDevice.ConnectInfo()
        network_spec.device.connectable.startConnected = \
            connectable['start_connected']
        network_spec.device.connectable.allowGuestControl = \
            connectable['allow_guest_control']
    return network_spec