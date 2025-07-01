def json2space(in_x, name=ROOT):
    """
    Change json to search space in hyperopt.

    Parameters
    ----------
    in_x : dict/list/str/int/float
        The part of json.
    name : str
        name could be ROOT, TYPE, VALUE or INDEX.
    """
    out_y = copy.deepcopy(in_x)
    if isinstance(in_x, dict):
        if TYPE in in_x.keys():
            _type = in_x[TYPE]
            name = name + '-' + _type
            _value = json2space(in_x[VALUE], name=name)
            if _type == 'choice':
                out_y = eval('hp.hp.'+_type)(name, _value)
            else:
                if _type in ['loguniform', 'qloguniform']:
                    _value[:2] = np.log(_value[:2])
                out_y = eval('hp.hp.' + _type)(name, *_value)
        else:
            out_y = dict()
            for key in in_x.keys():
                out_y[key] = json2space(in_x[key], name+'[%s]' % str(key))
    elif isinstance(in_x, list):
        out_y = list()
        for i, x_i in enumerate(in_x):
            out_y.append(json2space(x_i, name+'[%d]' % i))
    else:
        logger.info('in_x is not a dict or a list in json2space fuinction %s', str(in_x))
    return out_y