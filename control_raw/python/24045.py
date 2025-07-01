def _ordereddict2dict(input_ordered_dict):
    '''
    Convert ordered dictionary to a dictionary
    '''
    return salt.utils.json.loads(salt.utils.json.dumps(input_ordered_dict))