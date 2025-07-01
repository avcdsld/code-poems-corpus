def list_backups_dir(path, limit=None):
    '''
    Lists the previous versions of a directory backed up using Salt's :ref:`file
    state backup <file-state-backups>` system.

    path
        The directory on the minion to check for backups
    limit
        Limit the number of results to the most recent N backups

    CLI Example:

    .. code-block:: bash

        salt '*' file.list_backups_dir /foo/bar/baz/
    '''
    path = os.path.expanduser(path)

    try:
        limit = int(limit)
    except TypeError:
        pass
    except ValueError:
        log.error('file.list_backups_dir: \'limit\' value must be numeric')
        limit = None

    bkroot = _get_bkroot()
    parent_dir, basename = os.path.split(path)
    # Figure out full path of location of backup folder in minion cache
    bkdir = os.path.join(bkroot, parent_dir[1:])

    if not os.path.isdir(bkdir):
        return {}

    files = {}
    f = dict([(i, len(list(n))) for i, n in itertools.groupby([x.split("_")[0] for x in sorted(os.listdir(bkdir))])])
    ff = os.listdir(bkdir)
    for i, n in six.iteritems(f):
        ssfile = {}
        for x in sorted(ff):
            basename = x.split('_')[0]
            if i == basename:
                strpfmt = '{0}_%a_%b_%d_%H:%M:%S_%f_%Y'.format(basename)
                try:
                    timestamp = datetime.datetime.strptime(x, strpfmt)
                except ValueError:
                    # Folder didn't match the strp format string, so it's not a backup
                    # for this folder. Move on to the next one.
                    continue
                ssfile.setdefault(timestamp, {})['Backup Time'] = \
                    timestamp.strftime('%a %b %d %Y %H:%M:%S.%f')
                location = os.path.join(bkdir, x)
                ssfile[timestamp]['Size'] = os.stat(location).st_size
                ssfile[timestamp]['Location'] = location

        sfiles = dict(list(zip(list(range(n)), [ssfile[x] for x in sorted(ssfile, reverse=True)[:limit]])))
        sefiles = {i: sfiles}
        files.update(sefiles)
    return files