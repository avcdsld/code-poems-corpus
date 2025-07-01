def _apply_serial_port(serial_device_spec, key, operation='add'):
    '''
    Returns a vim.vm.device.VirtualSerialPort representing a serial port
    component

    serial_device_spec
        Serial device properties

    key
        Unique key of the device

    operation
        Add or edit the given device

    .. code-block:: bash

        serial_ports:
            adapter: 'Serial port 1'
            backing:
              type: uri
              uri: 'telnet://something:port'
              direction: <client|server>
              filename: 'service_uri'
            connectable:
              allow_guest_control: True
              start_connected: True
            yield: False
    '''
    log.trace('Creating serial port adapter=%s type=%s connectable=%s yield=%s',
              serial_device_spec['adapter'], serial_device_spec['type'],
              serial_device_spec['connectable'], serial_device_spec['yield'])
    device_spec = vim.vm.device.VirtualDeviceSpec()
    device_spec.device = vim.vm.device.VirtualSerialPort()
    if operation == 'add':
        device_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
    elif operation == 'edit':
        device_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit
    connect_info = vim.vm.device.VirtualDevice.ConnectInfo()
    type_backing = None

    if serial_device_spec['type'] == 'network':
        type_backing = vim.vm.device.VirtualSerialPort.URIBackingInfo()
        if 'uri' not in serial_device_spec['backing'].keys():
            raise ValueError('vSPC proxy URI not specified in config')
        if 'uri' not in serial_device_spec['backing'].keys():
            raise ValueError('vSPC Direction not specified in config')
        if 'filename' not in serial_device_spec['backing'].keys():
            raise ValueError('vSPC Filename not specified in config')
        type_backing.proxyURI = serial_device_spec['backing']['uri']
        type_backing.direction = serial_device_spec['backing']['direction']
        type_backing.serviceURI = serial_device_spec['backing']['filename']
    if serial_device_spec['type'] == 'pipe':
        type_backing = vim.vm.device.VirtualSerialPort.PipeBackingInfo()
    if serial_device_spec['type'] == 'file':
        type_backing = vim.vm.device.VirtualSerialPort.FileBackingInfo()
    if serial_device_spec['type'] == 'device':
        type_backing = vim.vm.device.VirtualSerialPort.DeviceBackingInfo()
    connect_info.allowGuestControl = \
        serial_device_spec['connectable']['allow_guest_control']
    connect_info.startConnected = \
        serial_device_spec['connectable']['start_connected']
    device_spec.device.backing = type_backing
    device_spec.device.connectable = connect_info
    device_spec.device.unitNumber = 1
    device_spec.device.key = key
    device_spec.device.yieldOnPoll = serial_device_spec['yield']

    return device_spec