def _dict_to_json_pretty(d, sort_keys=True):
    '''
    helper function to generate pretty printed json output
    '''
    return salt.utils.json.dumps(d, indent=4, separators=(',', ': '), sort_keys=sort_keys)