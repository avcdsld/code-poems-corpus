def _upstart_is_disabled(name):
    '''
    An Upstart service is assumed disabled if a manual stanza is
    placed in /etc/init/[name].override.
    NOTE: An Upstart service can also be disabled by placing "manual"
    in /etc/init/[name].conf.
    '''
    files = ['/etc/init/{0}.conf'.format(name), '/etc/init/{0}.override'.format(name)]
    for file_name in filter(os.path.isfile, files):
        with salt.utils.files.fopen(file_name) as fp_:
            if re.search(r'^\s*manual',
                         salt.utils.stringutils.to_unicode(fp_.read()),
                         re.MULTILINE):
                return True
    return False