def add_veth(name, interface_name, bridge=None, path=None):
    '''
    Add a veth to a container.
    Note : this function doesn't update the container config, just add the interface at runtime

    name
        Name of the container

    interface_name
        Name of the interface in the container

    bridge
        Name of the bridge to attach the interface to (facultative)

    CLI Examples:

    .. code-block:: bash

        salt '*' lxc.add_veth container_name eth1 br1
        salt '*' lxc.add_veth container_name eth1
    '''

    # Get container init PID
    pid = get_pid(name, path=path)

    # Generate a ramdom string for veth and ensure that is isn't present on the system
    while True:
        random_veth = 'veth'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        if random_veth not in __salt__['network.interfaces']().keys():
            break

    # Check prerequisites
    if not __salt__['file.directory_exists']('/var/run/'):
        raise CommandExecutionError('Directory /var/run required for lxc.add_veth doesn\'t exists')
    if not __salt__['file.file_exists']('/proc/{0}/ns/net'.format(pid)):
        raise CommandExecutionError('Proc file for container {0} network namespace doesn\'t exists'.format(name))

    if not __salt__['file.directory_exists']('/var/run/netns'):
        __salt__['file.mkdir']('/var/run/netns')

    # Ensure that the symlink is up to date (change on container restart)
    if __salt__['file.is_link']('/var/run/netns/{0}'.format(name)):
        __salt__['file.remove']('/var/run/netns/{0}'.format(name))

    __salt__['file.symlink']('/proc/{0}/ns/net'.format(pid), '/var/run/netns/{0}'.format(name))

    # Ensure that interface doesn't exists
    interface_exists = 0 == __salt__['cmd.retcode']('ip netns exec {netns} ip address list {interface}'.format(
            netns=name,
            interface=interface_name
        ))

    if interface_exists:
        raise CommandExecutionError('Interface {interface} already exists in {container}'.format(
                interface=interface_name,
                container=name
            ))

    # Create veth and bring it up
    if __salt__['cmd.retcode']('ip link add name {veth} type veth peer name {veth}_c'.format(veth=random_veth)) != 0:
        raise CommandExecutionError('Error while creating the veth pair {0}'.format(random_veth))
    if __salt__['cmd.retcode']('ip link set dev {0} up'.format(random_veth)) != 0:
        raise CommandExecutionError('Error while bringing up host-side veth {0}'.format(random_veth))

    # Attach it to the container
    attached = 0 == __salt__['cmd.retcode']('ip link set dev {veth}_c netns {container} name {interface_name}'.format(
            veth=random_veth,
            container=name,
            interface_name=interface_name
        ))
    if not attached:
        raise CommandExecutionError('Error while attaching the veth {veth} to container {container}'.format(
                veth=random_veth,
                container=name
            ))

    __salt__['file.remove']('/var/run/netns/{0}'.format(name))

    if bridge is not None:
        __salt__['bridge.addif'](bridge, random_veth)