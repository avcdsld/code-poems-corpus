def comment(name, regex, char='#', backup='.bak'):
    '''
    Comment out specified lines in a file.

    name
        The full path to the file to be edited
    regex
        A regular expression used to find the lines that are to be commented;
        this pattern will be wrapped in parenthesis and will move any
        preceding/trailing ``^`` or ``$`` characters outside the parenthesis
        (e.g., the pattern ``^foo$`` will be rewritten as ``^(foo)$``)
        Note that you _need_ the leading ^, otherwise each time you run
        highstate, another comment char will be inserted.
    char : ``#``
        The character to be inserted at the beginning of a line in order to
        comment it out
    backup : ``.bak``
        The file will be backed up before edit with this file extension

        .. warning::

            This backup will be overwritten each time ``sed`` / ``comment`` /
            ``uncomment`` is called. Meaning the backup will only be useful
            after the first invocation.

        Set to False/None to not keep a backup.

    Usage:

    .. code-block:: yaml

        /etc/fstab:
          file.comment:
            - regex: ^bind 127.0.0.1

    .. versionadded:: 0.9.5
    '''
    name = os.path.expanduser(name)

    ret = {'name': name,
           'changes': {},
           'result': False,
           'comment': ''}
    if not name:
        return _error(ret, 'Must provide name to file.comment')

    check_res, check_msg = _check_file(name)
    if not check_res:
        return _error(ret, check_msg)

    # remove (?i)-like flags, ^ and $
    unanchor_regex = re.sub(r'^(\(\?[iLmsux]\))?\^?(.*?)\$?$', r'\2', regex)

    comment_regex = char + unanchor_regex

    # Make sure the pattern appears in the file before continuing
    if not __salt__['file.search'](name, regex, multiline=True):
        if __salt__['file.search'](name, comment_regex, multiline=True):
            ret['comment'] = 'Pattern already commented'
            ret['result'] = True
            return ret
        else:
            return _error(ret, '{0}: Pattern not found'.format(unanchor_regex))

    if __opts__['test']:
        ret['changes'][name] = 'updated'
        ret['comment'] = 'File {0} is set to be updated'.format(name)
        ret['result'] = None
        return ret
    with salt.utils.files.fopen(name, 'rb') as fp_:
        slines = fp_.read()
        if six.PY3:
            slines = slines.decode(__salt_system_encoding__)
        slines = slines.splitlines(True)

    # Perform the edit
    __salt__['file.comment_line'](name, regex, char, True, backup)

    with salt.utils.files.fopen(name, 'rb') as fp_:
        nlines = fp_.read()
        if six.PY3:
            nlines = nlines.decode(__salt_system_encoding__)
        nlines = nlines.splitlines(True)

    # Check the result
    ret['result'] = __salt__['file.search'](name, unanchor_regex, multiline=True)

    if slines != nlines:
        if not __utils__['files.is_text'](name):
            ret['changes']['diff'] = 'Replace binary file'
        else:
            # Changes happened, add them
            ret['changes']['diff'] = (
                ''.join(difflib.unified_diff(slines, nlines))
            )

    if ret['result']:
        ret['comment'] = 'Commented lines successfully'
    else:
        ret['comment'] = 'Expected commented lines not found'

    return ret