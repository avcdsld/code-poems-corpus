def _generate_version(base_version):
    """Generate a version with information about the git repository"""
    pkg_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    if not _is_git_repo(pkg_dir) or not _have_git():
        return base_version

    if _is_release(pkg_dir, base_version) and not _is_dirty(pkg_dir):
        return base_version

    return "{base_version}+{short_sha}{dirty}".format(
        base_version=base_version,
        short_sha=_git_revision(pkg_dir).decode("utf-8")[0:6],
        dirty=".mod" if _is_dirty(pkg_dir) else "",
    )