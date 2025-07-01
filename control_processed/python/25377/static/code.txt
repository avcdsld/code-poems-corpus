def _delete_device(device):
    '''
    Returns a vim.vm.device.VirtualDeviceSpec specifying to remove a virtual
    machine device

    device
        Device data type object
    '''
    log.trace('Deleting device with type %s', type(device))
    device_spec = vim.vm.device.VirtualDeviceSpec()
    device_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.remove
    device_spec.device = device
    return device_spec