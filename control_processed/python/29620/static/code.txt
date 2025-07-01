def import_image(uuid, verbose=False):
    '''
    Import an image from the repository

    uuid : string
        uuid to import
    verbose : boolean (False)
        toggle verbose output

    CLI Example:

    .. code-block:: bash

        salt '*' imgadm.import e42f8c84-bbea-11e2-b920-078fab2aab1f [verbose=True]
    '''
    ret = {}
    cmd = 'imgadm import {0}'.format(uuid)
    res = __salt__['cmd.run_all'](cmd, python_shell=False)
    retcode = res['retcode']
    if retcode != 0:
        ret['Error'] = _exit_status(retcode)
        return ret

    uuid = docker_to_uuid(uuid)
    data = _parse_image_meta(get(uuid), verbose)
    return {uuid: data}