def tar(options, tarfile, sources=None, dest=None,
        cwd=None, template=None, runas=None):
    '''
    .. note::

        This function has changed for version 0.17.0. In prior versions, the
        ``cwd`` and ``template`` arguments must be specified, with the source
        directories/files coming as a space-separated list at the end of the
        command. Beginning with 0.17.0, ``sources`` must be a comma-separated
        list, and the ``cwd`` and ``template`` arguments are optional.

    Uses the tar command to pack, unpack, etc. tar files


    options
        Options to pass to the tar command

        .. versionchanged:: 2015.8.0

            The mandatory `-` prefixing has been removed.  An options string
            beginning with a `--long-option`, would have uncharacteristically
            needed its first `-` removed under the former scheme.

            Also, tar will parse its options differently if short options are
            used with or without a preceding `-`, so it is better to not
            confuse the user into thinking they're using the non-`-` format,
            when really they are using the with-`-` format.

    tarfile
        The filename of the tar archive to pack/unpack

    sources
        Comma delimited list of files to **pack** into the tarfile. Can also be
        passed as a Python list.

        .. versionchanged:: 2017.7.0
            Globbing is now supported for this argument

    dest
        The destination directory into which to **unpack** the tarfile

    cwd : None
        The directory in which the tar command should be executed. If not
        specified, will default to the home directory of the user under which
        the salt minion process is running.

    template : None
        Can be set to 'jinja' or another supported template engine to render
        the command arguments before execution:

        .. code-block:: bash

            salt '*' archive.tar cjvf /tmp/salt.tar.bz2 {{grains.saltpath}} template=jinja

    CLI Examples:

    .. code-block:: bash

        # Create a tarfile
        salt '*' archive.tar cjvf /tmp/tarfile.tar.bz2 /tmp/file_1,/tmp/file_2
        # Create a tarfile using globbing (2017.7.0 and later)
        salt '*' archive.tar cjvf /tmp/tarfile.tar.bz2 '/tmp/file_*'
        # Unpack a tarfile
        salt '*' archive.tar xf foo.tar dest=/target/directory
    '''
    if not options:
        # Catch instances were people pass an empty string for the "options"
        # argument. Someone would have to be really silly to do this, but we
        # should at least let them know of their silliness.
        raise SaltInvocationError('Tar options can not be empty')

    cmd = ['tar']
    if options:
        cmd.extend(options.split())

    cmd.extend(['{0}'.format(tarfile)])
    cmd.extend(_expand_sources(sources))
    if dest:
        cmd.extend(['-C', '{0}'.format(dest)])

    return __salt__['cmd.run'](cmd,
                               cwd=cwd,
                               template=template,
                               runas=runas,
                               python_shell=False).splitlines()