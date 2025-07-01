def merge(cwd,
          rev=None,
          opts='',
          git_opts='',
          user=None,
          password=None,
          identity=None,
          ignore_retcode=False,
          output_encoding=None,
          **kwargs):
    '''
    Interface to `git-merge(1)`_

    cwd
        The path to the git checkout

    rev
        Revision to merge into the current branch. If not specified, the remote
        tracking branch will be merged.

        .. versionadded:: 2015.8.0

    opts
        Any additional options to add to the command line, in a single string

        .. note::
            On the Salt CLI, if the opts are preceded with a dash, it is
            necessary to precede them with ``opts=`` (as in the CLI examples
            below) to avoid causing errors with Salt's own argument parsing.

    git_opts
        Any additional options to add to git command itself (not the ``merge``
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
        Path to a private key to use for ssh URLs. Salt will not attempt to use
        passphrase-protected keys unless invoked from the minion using
        ``salt-call``, to prevent blocking waiting for user input. Key can also
        be specified as a SaltStack file server URL, eg.
        ``salt://location/identity_file``.

        .. note::
            For greater security with passphraseless private keys, see the
            `sshd(8)`_ manpage for information on securing the keypair from the
            remote side in the ``authorized_keys`` file.

            .. _`sshd(8)`: http://www.man7.org/linux/man-pages/man8/sshd.8.html#AUTHORIZED_KEYS_FILE_FORMAT

        .. versionadded:: 2018.3.5,2019.2.1,Neon

    ignore_retcode : False
        If ``True``, do not log an error to the minion log if the git command
        returns a nonzero exit status.

        .. versionadded:: 2015.8.0

    output_encoding
        Use this option to specify which encoding to use to decode the output
        from any git commands which are run. This should not be needed in most
        cases.

        .. note::
            This should only be needed if the files in the repository were
            created with filenames using an encoding other than UTF-8 to handle
            Unicode characters.

        .. versionadded:: 2018.3.1

    .. _`git-merge(1)`: http://git-scm.com/docs/git-merge

    CLI Example:

    .. code-block:: bash

        # Fetch first...
        salt myminion git.fetch /path/to/repo
        # ... then merge the remote tracking branch
        salt myminion git.merge /path/to/repo
        # .. or merge another rev
        salt myminion git.merge /path/to/repo rev=upstream/foo
    '''
    kwargs = salt.utils.args.clean_kwargs(**kwargs)
    if kwargs:
        salt.utils.args.invalid_kwargs(kwargs)

    cwd = _expand_path(cwd, user)
    command = ['git'] + _format_git_opts(git_opts)
    command.append('merge')
    command.extend(_format_opts(opts))
    if rev:
        command.append(rev)

    return _git_run(command,
                    cwd=cwd,
                    user=user,
                    password=password,
                    identity=identity,
                    ignore_retcode=ignore_retcode,
                    output_encoding=output_encoding)['stdout']