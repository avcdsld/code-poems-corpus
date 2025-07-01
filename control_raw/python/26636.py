def _check_pillar(kwargs, pillar=None):
    '''
    Check the pillar for errors, refuse to run the state if there are errors
    in the pillar and return the pillar errors
    '''
    if kwargs.get('force'):
        return True
    pillar_dict = pillar if pillar is not None else __pillar__
    if '_errors' in pillar_dict:
        return False
    return True