def get_hg_revision(repopath):
    """Return Mercurial revision for the repository located at repopath
       Result is a tuple (global, local, branch), with None values on error
       For example:
           >>> get_hg_revision(".")
           ('eba7273c69df+', '2015+', 'default')
    """
    try:
        assert osp.isdir(osp.join(repopath, '.hg'))
        proc = programs.run_program('hg', ['id', '-nib', repopath])
        output, _err = proc.communicate()
        # output is now: ('eba7273c69df+ 2015+ default\n', None)
        # Split 2 times max to allow spaces in branch names.
        return tuple(output.decode().strip().split(None, 2))
    except (subprocess.CalledProcessError, AssertionError, AttributeError,
            OSError):
        return (None, None, None)