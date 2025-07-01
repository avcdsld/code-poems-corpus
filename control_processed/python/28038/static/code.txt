def fetch(cwd,
          remote=None,
          force=False,
          refspecs=None,
          opts='',
          git_opts='',
          user=None,
          password=None,
          identity=None,
          ignore_retcode=False,
          saltenv='base',
          output_encoding=None):
    '''
    .. versionchanged:: 2015.8.2
        Return data is now a dictionary containing information on branches and
        tags that were added/updated

    Interface to `git-fetch(1)`_

    cwd
        The path to the git checkout

    remote
        Optional remote name to fetch. If not passed, then git will use its
        default behavior (as detailed in `git-fetch(1)`_).

        .. versionadded:: 2015.8.0

    force
        Force the fetch even when it is not a fast-forward.

        .. versionadded:: 2015.8.0

    refspecs
        Override the refspec(s) configured for the remote with this argument.
        Multiple refspecs can be passed, comma-separated.

        .. versionadded:: 2015.8.0

    opts
        Any additional options to add to the command line, in a single string

        .. note::
            On the Salt CLI, if the opts are preceded with a dash, it is
            necessary to precede them with ``opts=`` (as in the CLI examples
            below) to avoid causing errors with Salt's own argument parsing.

    git_opts
        Any additional options to add to git command itself (not the ``fetch``
        subcommand), in a single string. This is useful for passing ``-c`` to
        run git with temporary changes to the git configuration.

        .. versionadded:: 2017.7.0

        .. note::
            This is only supported in git 1.7.2 and newer.

    user
        User under which to run the git command. By default, the command is run
        by the user under which the minion is running.

    password
        Windows only. Required when specifying ``user``. This parameter will be
        ignored on non-Windows platforms.

      .. versionadded:: 2016.3.4

    identity
        Path to a private key to use for ssh URLs

        .. warning::

            Unless Salt is invoked from the minion using ``salt-call``, the
            key(s) must be passphraseless. For greater security with
            passphraseless private keys, see the `sshd(8)`_ manpage for
            information on securing the keypair from the remote side in the
            ``authorized_keys`` file.

            .. _`sshd(8)`: http://www.man7.org/linux/man-pages/man8/sshd.8.html#AUTHORIZED_KEYS_FILE_FORMAT

        .. versionchanged:: 2015.8.7

            Salt will no longer attempt to use passphrase-protected keys unless
            invoked from the minion using ``salt-call``, to prevent blocking
            waiting for user input.

        Key can also be specified as a SaltStack file server URL, eg. salt://location/identity_file

        .. versionchanged:: 2016.3.0

    ignore_retcode : False
        If ``True``, do not log an error to the minion log if the git command
        returns a nonzero exit status.

        .. versionadded:: 2015.8.0

    saltenv
        The default salt environment to pull sls files from

        .. versionadded:: 2016.3.1

    output_encoding
        Use this option to specify which encoding to use to decode the output
        from any git commands which are run. This should not be needed in most
        cases.

        .. note::
            This should only be needed if the files in the repository were
            created with filenames using an encoding other than UTF-8 to handle
            Unicode characters.

        .. versionadded:: 2018.3.1

    .. _`git-fetch(1)`: http://git-scm.com/docs/git-fetch

    CLI Example:

    .. code-block:: bash

        salt myminion git.fetch /path/to/repo upstream
        salt myminion git.fetch /path/to/repo identity=/root/.ssh/id_rsa
    '''
    cwd = _expand_path(cwd, user)
    command = ['git'] + _format_git_opts(git_opts)
    command.append('fetch')
    if force:
        command.append('--force')
    command.extend(
        [x for x in _format_opts(opts) if x not in ('-f', '--force')]
    )
    if remote:
        command.append(remote)
    if refspecs is not None:
        if not isinstance(refspecs, (list, tuple)):
            try:
                refspecs = refspecs.split(',')
            except AttributeError:
                refspecs = six.text_type(refspecs).split(',')
        refspecs = salt.utils.data.stringify(refspecs)
        command.extend(refspecs)
    output = _git_run(command,
                      cwd=cwd,
                      user=user,
                      password=password,
                      identity=identity,
                      ignore_retcode=ignore_retcode,
                      redirect_stderr=True,
                      saltenv=saltenv,
                      output_encoding=output_encoding)['stdout']

    update_re = re.compile(
        r'[\s*]*(?:([0-9a-f]+)\.\.([0-9a-f]+)|'
        r'\[(?:new (tag|branch)|tag update)\])\s+(.+)->'
    )
    ret = {}
    for line in salt.utils.itertools.split(output, '\n'):
        match = update_re.match(line)
        if match:
            old_sha, new_sha, new_ref_type, ref_name = \
                match.groups()
            ref_name = ref_name.rstrip()
            if new_ref_type is not None:
                # ref is a new tag/branch
                ref_key = 'new tags' \
                    if new_ref_type == 'tag' \
                    else 'new branches'
                ret.setdefault(ref_key, []).append(ref_name)
            elif old_sha is not None:
                # ref is a branch update
                ret.setdefault('updated branches', {})[ref_name] = \
                    {'old': old_sha, 'new': new_sha}
            else:
                # ref is an updated tag
                ret.setdefault('updated tags', []).append(ref_name)
    return ret