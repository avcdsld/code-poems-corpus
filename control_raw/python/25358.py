def _apply_sata_controller_config(sata_controller_label, operation,
                                  key, bus_number=0):
    '''
    Returns a vim.vm.device.VirtualDeviceSpec object specifying to add/edit a
    SATA controller

    sata_controller_label
        Controller label of the SATA adapter

    operation
        Type of operation: add or edit

    key
        Unique key of the device

    bus_number
        Device bus number property
    '''
    log.trace('Configuring SATA controller sata_controller_label=%s',
              sata_controller_label)
    sata_spec = vim.vm.device.VirtualDeviceSpec()
    sata_spec.device = vim.vm.device.VirtualAHCIController()
    if operation == 'add':
        sata_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
    elif operation == 'edit':
        sata_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit
    sata_spec.device.key = key
    sata_spec.device.controllerKey = 100
    sata_spec.device.busNumber = bus_number
    if sata_controller_label:
        sata_spec.device.deviceInfo = vim.Description()
        sata_spec.device.deviceInfo.label = sata_controller_label
        sata_spec.device.deviceInfo.summary = sata_controller_label
    return sata_spec