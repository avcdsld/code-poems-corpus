def _parse_config(conf, slot=None):
    '''
    Recursively goes through config structure and builds final Apache configuration

    :param conf: defined config structure
    :param slot: name of section container if needed
    '''
    ret = cStringIO()
    if isinstance(conf, six.string_types):
        if slot:
            print('{0} {1}'.format(slot, conf), file=ret, end='')
        else:
            print('{0}'.format(conf), file=ret, end='')
    elif isinstance(conf, list):
        is_section = False
        for item in conf:
            if 'this' in item:
                is_section = True
                slot_this = six.text_type(item['this'])
        if is_section:
            print('<{0} {1}>'.format(slot, slot_this), file=ret)
            for item in conf:
                for key, val in item.items():
                    if key != 'this':
                        print(_parse_config(val, six.text_type(key)), file=ret)
            print('</{0}>'.format(slot), file=ret)
        else:
            for value in conf:
                print(_parse_config(value, six.text_type(slot)), file=ret)
    elif isinstance(conf, dict):
        try:
            print('<{0} {1}>'.format(slot, conf['this']), file=ret)
        except KeyError:
            raise SaltException('Apache section container "<{0}>" expects attribute. '
                                'Specify it using key "this".'.format(slot))
        for key, value in six.iteritems(conf):
            if key != 'this':
                if isinstance(value, six.string_types):
                    print('{0} {1}'.format(key, value), file=ret)
                elif isinstance(value, list):
                    print(_parse_config(value, key), file=ret)
                elif isinstance(value, dict):
                    print(_parse_config(value, key), file=ret)
        print('</{0}>'.format(slot), file=ret)

    ret.seek(0)
    return ret.read()