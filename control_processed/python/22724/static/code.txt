def _kernel_versions_debian():
    '''
    Last installed kernel name, for Debian based systems.

    Returns:
            List with possible names of last installed kernel
            as they are probably interpreted in output of `uname -a` command.
    '''
    kernel_get_selections = __salt__['cmd.run']('dpkg --get-selections linux-image-*')
    kernels = []
    kernel_versions = []
    for line in kernel_get_selections.splitlines():
        kernels.append(line)

    try:
        kernel = kernels[-2]
    except IndexError:
        kernel = kernels[0]

    kernel = kernel.rstrip('\t\tinstall')

    kernel_get_version = __salt__['cmd.run']('apt-cache policy ' + kernel)

    for line in kernel_get_version.splitlines():
        if line.startswith('  Installed: '):
            kernel_v = line.strip('  Installed: ')
            kernel_versions.append(kernel_v)
            break

    if __grains__['os'] == 'Ubuntu':
        kernel_v = kernel_versions[0].rsplit('.', 1)
        kernel_ubuntu_generic = kernel_v[0] + '-generic #' + kernel_v[1]
        kernel_ubuntu_lowlatency = kernel_v[0] + '-lowlatency #' + kernel_v[1]
        kernel_versions.extend([kernel_ubuntu_generic, kernel_ubuntu_lowlatency])

    return kernel_versions