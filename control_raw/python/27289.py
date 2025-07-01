def ext_pillar(minion_id,  # pylint: disable=W0613
               pillar,  # pylint: disable=W0613
               conf):
    '''
    Parse varstack data and return the result
    '''
    vs = varstack.Varstack(config_filename=conf)
    return vs.evaluate(__grains__)