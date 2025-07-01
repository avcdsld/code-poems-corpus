def properties(obj, type=None, set=None):
    '''
    List properties for given btrfs object. The object can be path of BTRFS device,
    mount point, or any directories/files inside the BTRFS filesystem.

    General options:

    * **type**: Possible types are s[ubvol], f[ilesystem], i[node] and d[evice].
    * **force**: Force overwrite existing filesystem on the disk
    * **set**: <key=value,key1=value1...> Options for a filesystem properties.

    CLI Example:

    .. code-block:: bash

        salt '*' btrfs.properties /mountpoint
        salt '*' btrfs.properties /dev/sda1 type=subvol set='ro=false,label="My Storage"'
    '''
    if type and type not in ['s', 'subvol', 'f', 'filesystem', 'i', 'inode', 'd', 'device']:
        raise CommandExecutionError("Unknown property type: \"{0}\" specified".format(type))

    cmd = ['btrfs']
    cmd.append('property')
    cmd.append(set and 'set' or 'list')
    if type:
        cmd.append('-t{0}'.format(type))
    cmd.append(obj)

    if set:
        try:
            for key, value in [[item.strip() for item in keyset.split("=")]
                               for keyset in set.split(",")]:
                cmd.append(key)
                cmd.append(value)
        except Exception as ex:
            raise CommandExecutionError(ex)

    out = __salt__['cmd.run_all'](' '.join(cmd))
    salt.utils.fsutils._verify_run(out)

    if not set:
        ret = {}
        for prop, descr in six.iteritems(_parse_proplist(out['stdout'])):
            ret[prop] = {'description': descr}
            value = __salt__['cmd.run_all'](
                "btrfs property get {0} {1}".format(obj, prop))['stdout']
            ret[prop]['value'] = value and value.split("=")[-1] or "N/A"

        return ret