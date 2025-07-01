def _get_info(info, name):
    """ get/create the info for this name """
    try:
        idx = info[name]
    except KeyError:
        idx = info[name] = dict()
    return idx