def _get_pillar_cfg(pillar_key,
                    pillarenv=None,
                    saltenv=None):
    '''
    Retrieve the pillar data from the right environment.
    '''
    pillar_cfg = __salt__['pillar.get'](pillar_key,
                                        pillarenv=pillarenv,
                                        saltenv=saltenv)
    return pillar_cfg