def _apply_cpu_config(config_spec, cpu_props):
    '''
    Sets CPU core count to the given value

    config_spec
        vm.ConfigSpec object

    cpu_props
        CPU properties dict
    '''
    log.trace('Configuring virtual machine CPU '
              'settings cpu_props=%s', cpu_props)
    if 'count' in cpu_props:
        config_spec.numCPUs = int(cpu_props['count'])
    if 'cores_per_socket' in cpu_props:
        config_spec.numCoresPerSocket = int(cpu_props['cores_per_socket'])
    if 'nested' in cpu_props and cpu_props['nested']:
        config_spec.nestedHVEnabled = cpu_props['nested']  # True
    if 'hotadd' in cpu_props and cpu_props['hotadd']:
        config_spec.cpuHotAddEnabled = cpu_props['hotadd']  # True
    if 'hotremove' in cpu_props and cpu_props['hotremove']:
        config_spec.cpuHotRemoveEnabled = cpu_props['hotremove']