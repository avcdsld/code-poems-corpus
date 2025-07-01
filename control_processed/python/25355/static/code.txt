def _create_ide_controllers(ide_controllers):
    '''
    Returns a list of vim.vm.device.VirtualDeviceSpec objects representing
    IDE controllers

    ide_controllers
        IDE properties
    '''
    ide_ctrls = []
    keys = range(-200, -250, -1)
    if ide_controllers:
        devs = [ide['adapter'] for ide in ide_controllers]
        log.trace('Creating IDE controllers %s', devs)
        for ide, key in zip(ide_controllers, keys):
            ide_ctrls.append(_apply_ide_controller_config(
                ide['adapter'], 'add', key, abs(key + 200)))
    return ide_ctrls