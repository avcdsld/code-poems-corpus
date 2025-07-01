def _parse_conf(conf_file=_DEFAULT_CONF):
    '''
    Parse a logrotate configuration file.

    Includes will also be parsed, and their configuration will be stored in the
    return dict, as if they were part of the main config file. A dict of which
    configs came from which includes will be stored in the 'include files' dict
    inside the return dict, for later reference by the user or module.
    '''
    ret = {}
    mode = 'single'
    multi_names = []
    multi = {}
    prev_comps = None

    with salt.utils.files.fopen(conf_file, 'r') as ifile:
        for line in ifile:
            line = salt.utils.stringutils.to_unicode(line).strip()
            if not line:
                continue
            if line.startswith('#'):
                continue

            comps = line.split()
            if '{' in line and '}' not in line:
                mode = 'multi'
                if len(comps) == 1 and prev_comps:
                    multi_names = prev_comps
                else:
                    multi_names = comps
                    multi_names.pop()
                continue
            if '}' in line:
                mode = 'single'
                for multi_name in multi_names:
                    ret[multi_name] = multi
                multi_names = []
                multi = {}
                continue

            if mode == 'single':
                key = ret
            else:
                key = multi

            if comps[0] == 'include':
                if 'include files' not in ret:
                    ret['include files'] = {}
                for include in os.listdir(comps[1]):
                    if include not in ret['include files']:
                        ret['include files'][include] = []

                    include_path = os.path.join(comps[1], include)
                    include_conf = _parse_conf(include_path)

                    for file_key in include_conf:
                        ret[file_key] = include_conf[file_key]
                        ret['include files'][include].append(file_key)

            prev_comps = comps
            if len(comps) > 2:
                key[comps[0]] = ' '.join(comps[1:])
            elif len(comps) > 1:
                key[comps[0]] = _convert_if_int(comps[1])
            else:
                key[comps[0]] = True
    return ret