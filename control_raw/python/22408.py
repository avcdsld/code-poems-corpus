def comment_line(path,
                 regex,
                 char='#',
                 cmnt=True,
                 backup='.bak'):
    r'''
    Comment or Uncomment a line in a text file.

    :param path: string
        The full path to the text file.

    :param regex: string
        A regex expression that begins with ``^`` that will find the line you wish
        to comment. Can be as simple as ``^color =``

    :param char: string
        The character used to comment a line in the type of file you're referencing.
        Default is ``#``

    :param cmnt: boolean
        True to comment the line. False to uncomment the line. Default is True.

    :param backup: string
        The file extension to give the backup file. Default is ``.bak``
        Set to False/None to not keep a backup.

    :return: boolean
        Returns True if successful, False if not

    CLI Example:

    The following example will comment out the ``pcspkr`` line in the
    ``/etc/modules`` file using the default ``#`` character and create a backup
    file named ``modules.bak``

    .. code-block:: bash

        salt '*' file.comment_line '/etc/modules' '^pcspkr'


    CLI Example:

    The following example will uncomment the ``log_level`` setting in ``minion``
    config file if it is set to either ``warning``, ``info``, or ``debug`` using
    the ``#`` character and create a backup file named ``minion.bk``

    .. code-block:: bash

        salt '*' file.comment_line 'C:\salt\conf\minion' '^log_level: (warning|info|debug)' '#' False '.bk'
    '''
    # Get the regex for comment or uncomment
    if cmnt:
        regex = '{0}({1}){2}'.format(
                '^' if regex.startswith('^') else '',
                regex.lstrip('^').rstrip('$'),
                '$' if regex.endswith('$') else '')
    else:
        regex = r'^{0}\s*({1}){2}'.format(
                char,
                regex.lstrip('^').rstrip('$'),
                '$' if regex.endswith('$') else '')

    # Load the real path to the file
    path = os.path.realpath(os.path.expanduser(path))

    # Make sure the file exists
    if not os.path.isfile(path):
        raise SaltInvocationError('File not found: {0}'.format(path))

    # Make sure it is a text file
    if not __utils__['files.is_text'](path):
        raise SaltInvocationError(
            'Cannot perform string replacements on a binary file: {0}'.format(path))

    # First check the whole file, determine whether to make the replacement
    # Searching first avoids modifying the time stamp if there are no changes
    found = False
    # Dictionaries for comparing changes
    orig_file = []
    new_file = []
    # Buffer size for fopen
    bufsize = os.path.getsize(path)
    try:
        # Use a read-only handle to open the file
        with salt.utils.files.fopen(path,
                                    mode='rb',
                                    buffering=bufsize) as r_file:
            # Loop through each line of the file and look for a match
            for line in r_file:
                # Is it in this line
                line = salt.utils.stringutils.to_unicode(line)
                if re.match(regex, line):
                    # Load lines into dictionaries, set found to True
                    orig_file.append(line)
                    if cmnt:
                        new_file.append('{0}{1}'.format(char, line))
                    else:
                        new_file.append(line.lstrip(char))
                    found = True
    except (OSError, IOError) as exc:
        raise CommandExecutionError(
            "Unable to open file '{0}'. "
            "Exception: {1}".format(path, exc)
        )

    # We've searched the whole file. If we didn't find anything, return False
    if not found:
        return False

    if not salt.utils.platform.is_windows():
        pre_user = get_user(path)
        pre_group = get_group(path)
        pre_mode = salt.utils.files.normalize_mode(get_mode(path))

    # Create a copy to read from and to use as a backup later
    try:
        temp_file = _mkstemp_copy(path=path, preserve_inode=False)
    except (OSError, IOError) as exc:
        raise CommandExecutionError("Exception: {0}".format(exc))

    try:
        # Open the file in write mode
        mode = 'wb' if six.PY2 and salt.utils.platform.is_windows() else 'w'
        with salt.utils.files.fopen(path,
                                    mode=mode,
                                    buffering=bufsize) as w_file:
            try:
                # Open the temp file in read mode
                with salt.utils.files.fopen(temp_file,
                                            mode='rb',
                                            buffering=bufsize) as r_file:
                    # Loop through each line of the file and look for a match
                    for line in r_file:
                        line = salt.utils.stringutils.to_unicode(line)
                        try:
                            # Is it in this line
                            if re.match(regex, line):
                                # Write the new line
                                if cmnt:
                                    wline = '{0}{1}'.format(char, line)
                                else:
                                    wline = line.lstrip(char)
                            else:
                                # Write the existing line (no change)
                                wline = line
                            wline = salt.utils.stringutils.to_bytes(wline) \
                                if six.PY2 and salt.utils.platform.is_windows() \
                                else salt.utils.stringutils.to_str(wline)
                            w_file.write(wline)
                        except (OSError, IOError) as exc:
                            raise CommandExecutionError(
                                "Unable to write file '{0}'. Contents may "
                                "be truncated. Temporary file contains copy "
                                "at '{1}'. "
                                "Exception: {2}".format(path, temp_file, exc)
                            )
            except (OSError, IOError) as exc:
                raise CommandExecutionError("Exception: {0}".format(exc))
    except (OSError, IOError) as exc:
        raise CommandExecutionError("Exception: {0}".format(exc))

    if backup:
        # Move the backup file to the original directory
        backup_name = '{0}{1}'.format(path, backup)
        try:
            shutil.move(temp_file, backup_name)
        except (OSError, IOError) as exc:
            raise CommandExecutionError(
                "Unable to move the temp file '{0}' to the "
                "backup file '{1}'. "
                "Exception: {2}".format(path, temp_file, exc)
            )
    else:
        os.remove(temp_file)

    if not salt.utils.platform.is_windows():
        check_perms(path, None, pre_user, pre_group, pre_mode)

    # Return a diff using the two dictionaries
    return __utils__['stringutils.get_diff'](orig_file, new_file)