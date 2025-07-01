def _getpwnam(name, root=None):
    '''
    Alternative implementation for getpwnam, that use only /etc/passwd
    '''
    root = '/' if not root else root
    passwd = os.path.join(root, 'etc/passwd')
    with salt.utils.files.fopen(passwd) as fp_:
        for line in fp_:
            line = salt.utils.stringutils.to_unicode(line)
            comps = line.strip().split(':')
            if comps[0] == name:
                # Generate a getpwnam compatible output
                comps[2], comps[3] = int(comps[2]), int(comps[3])
                return pwd.struct_passwd(comps)
    raise KeyError