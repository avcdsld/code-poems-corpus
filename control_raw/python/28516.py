def ext_pillar(minion_id, pillar, function, **kwargs):
    '''
    Grabs external pillar data based on configured function
    '''
    if function.startswith('_') or function not in globals():
        return {}
    # Call specified function to pull redis data
    return globals()[function](minion_id, pillar, **kwargs)