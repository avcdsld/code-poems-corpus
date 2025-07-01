def start_resolver(finder=None, wheel_cache=None):
    """Context manager to produce a resolver.

    :param finder: A package finder to use for searching the index
    :type finder: :class:`~pip._internal.index.PackageFinder`
    :return: A 3-tuple of finder, preparer, resolver
    :rtype: (:class:`~pip._internal.operations.prepare.RequirementPreparer`, :class:`~pip._internal.resolve.Resolver`)
    """

    pip_command = get_pip_command()
    pip_options = get_pip_options(pip_command=pip_command)

    if not finder:
        finder = get_finder(pip_command=pip_command, pip_options=pip_options)

    if not wheel_cache:
        wheel_cache = WHEEL_CACHE
    _ensure_dir(fs_str(os.path.join(wheel_cache.cache_dir, "wheels")))

    download_dir = PKGS_DOWNLOAD_DIR
    _ensure_dir(download_dir)

    _build_dir = create_tracked_tempdir(fs_str("build"))
    _source_dir = create_tracked_tempdir(fs_str("source"))
    preparer = partialclass(
        pip_shims.shims.RequirementPreparer,
        build_dir=_build_dir,
        src_dir=_source_dir,
        download_dir=download_dir,
        wheel_download_dir=WHEEL_DOWNLOAD_DIR,
        progress_bar="off",
        build_isolation=False,
    )
    resolver = partialclass(
        pip_shims.shims.Resolver,
        finder=finder,
        session=finder.session,
        upgrade_strategy="to-satisfy-only",
        force_reinstall=True,
        ignore_dependencies=False,
        ignore_requires_python=True,
        ignore_installed=True,
        isolated=False,
        wheel_cache=wheel_cache,
        use_user_site=False,
    )
    try:
        if packaging.version.parse(pip_shims.shims.pip_version) >= packaging.version.parse('18'):
            with pip_shims.shims.RequirementTracker() as req_tracker:
                preparer = preparer(req_tracker=req_tracker)
                yield resolver(preparer=preparer)
        else:
            preparer = preparer()
            yield resolver(preparer=preparer)
    finally:
        finder.session.close()