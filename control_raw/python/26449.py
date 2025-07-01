def create(zone, brand, zonepath, force=False):
    '''
    Create an in-memory configuration for the specified zone.

    zone : string
        name of zone
    brand : string
        brand name
    zonepath : string
        path of zone
    force : boolean
        overwrite configuration

    CLI Example:

    .. code-block:: bash

        salt '*' zonecfg.create deathscythe ipkg /zones/deathscythe
    '''
    ret = {'status': True}

    # write config
    cfg_file = salt.utils.files.mkstemp()
    with salt.utils.files.fpopen(cfg_file, 'w+', mode=0o600) as fp_:
        fp_.write("create -b -F\n" if force else "create -b\n")
        fp_.write("set brand={0}\n".format(_sanitize_value(brand)))
        fp_.write("set zonepath={0}\n".format(_sanitize_value(zonepath)))

    # create
    if not __salt__['file.directory_exists'](zonepath):
        __salt__['file.makedirs_perms'](zonepath if zonepath[-1] == '/' else '{0}/'.format(zonepath), mode='0700')

    _dump_cfg(cfg_file)
    res = __salt__['cmd.run_all']('zonecfg -z {zone} -f {cfg}'.format(
        zone=zone,
        cfg=cfg_file,
    ))
    ret['status'] = res['retcode'] == 0
    ret['message'] = res['stdout'] if ret['status'] else res['stderr']
    if ret['message'] == '':
        del ret['message']
    else:
        ret['message'] = _clean_message(ret['message'])

    # cleanup config file
    if __salt__['file.file_exists'](cfg_file):
        __salt__['file.remove'](cfg_file)

    return ret