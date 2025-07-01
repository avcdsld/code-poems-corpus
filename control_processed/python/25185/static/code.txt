def set_password(name, password, use_usermod=False, root=None):
    '''
    Set the password for a named user. The password must be a properly defined
    hash. The password hash can be generated with this command:

    ``python -c "import crypt; print crypt.crypt('password',
    '\\$6\\$SALTsalt')"``

    ``SALTsalt`` is the 8-character crpytographic salt. Valid characters in the
    salt are ``.``, ``/``, and any alphanumeric character.

    Keep in mind that the $6 represents a sha512 hash, if your OS is using a
    different hashing algorithm this needs to be changed accordingly

    name
        User to set the password

    password
        Password already hashed

    use_usermod
        Use usermod command to better compatibility

    root
        Directory to chroot into

    CLI Example:

    .. code-block:: bash

        salt '*' shadow.set_password root '$1$UYCIxa628.9qXjpQCjM4a..'
    '''
    if not salt.utils.data.is_true(use_usermod):
        # Edit the shadow file directly
        # ALT Linux uses tcb to store password hashes. More information found
        # in manpage (http://docs.altlinux.org/manpages/tcb.5.html)
        if __grains__['os'] == 'ALT':
            s_file = '/etc/tcb/{0}/shadow'.format(name)
        else:
            s_file = '/etc/shadow'
        if root:
            s_file = os.path.join(root, os.path.relpath(s_file, os.path.sep))

        ret = {}
        if not os.path.isfile(s_file):
            return ret
        lines = []
        with salt.utils.files.fopen(s_file, 'rb') as fp_:
            for line in fp_:
                line = salt.utils.stringutils.to_unicode(line)
                comps = line.strip().split(':')
                if comps[0] != name:
                    lines.append(line)
                    continue
                changed_date = datetime.datetime.today() - datetime.datetime(1970, 1, 1)
                comps[1] = password
                comps[2] = six.text_type(changed_date.days)
                line = ':'.join(comps)
                lines.append('{0}\n'.format(line))
        with salt.utils.files.fopen(s_file, 'w+') as fp_:
            lines = [salt.utils.stringutils.to_str(_l) for _l in lines]
            fp_.writelines(lines)
        uinfo = info(name, root=root)
        return uinfo['passwd'] == password
    else:
        # Use usermod -p (less secure, but more feature-complete)
        cmd = ['usermod']
        if root is not None:
            cmd.extend(('-R', root))
        cmd.extend(('-p', password, name))

        __salt__['cmd.run'](cmd, python_shell=False, output_loglevel='quiet')
        uinfo = info(name, root=root)
        return uinfo['passwd'] == password