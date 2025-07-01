def _stringlist_to_dictionary(input_string):
    '''
    Convert a stringlist (comma separated settings) to a dictionary

    The result of the string setting1=value1,setting2=value2 will be a python dictionary:

    {'setting1':'value1','setting2':'value2'}
    '''
    li = str(input_string).split(',')
    ret = {}
    for item in li:
        pair = str(item).replace(' ', '').split('=')
        if len(pair) != 2:
            log.warning('Cannot process stringlist item %s', item)
            continue

        ret[pair[0]] = pair[1]
    return ret