def pip_version_check(session, options):
    # type: (PipSession, optparse.Values) -> None
    """Check for an update for pip.

    Limit the frequency of checks to once per week. State is stored either in
    the active virtualenv or in the user's USER_CACHE_DIR keyed off the prefix
    of the pip script path.
    """
    installed_version = get_installed_version("pip")
    if not installed_version:
        return

    pip_version = packaging_version.parse(installed_version)
    pypi_version = None

    try:
        state = SelfCheckState(cache_dir=options.cache_dir)

        current_time = datetime.datetime.utcnow()
        # Determine if we need to refresh the state
        if "last_check" in state.state and "pypi_version" in state.state:
            last_check = datetime.datetime.strptime(
                state.state["last_check"],
                SELFCHECK_DATE_FMT
            )
            if (current_time - last_check).total_seconds() < 7 * 24 * 60 * 60:
                pypi_version = state.state["pypi_version"]

        # Refresh the version if we need to or just see if we need to warn
        if pypi_version is None:
            # Lets use PackageFinder to see what the latest pip version is
            finder = PackageFinder(
                find_links=options.find_links,
                index_urls=[options.index_url] + options.extra_index_urls,
                allow_all_prereleases=False,  # Explicitly set to False
                trusted_hosts=options.trusted_hosts,
                session=session,
            )
            all_candidates = finder.find_all_candidates("pip")
            if not all_candidates:
                return
            pypi_version = str(
                max(all_candidates, key=lambda c: c.version).version
            )

            # save that we've performed a check
            state.save(pypi_version, current_time)

        remote_version = packaging_version.parse(pypi_version)

        # Determine if our pypi_version is older
        if (pip_version < remote_version and
                pip_version.base_version != remote_version.base_version and
                was_installed_by_pip('pip')):
            # Advise "python -m pip" on Windows to avoid issues
            # with overwriting pip.exe.
            if WINDOWS:
                pip_cmd = "python -m pip"
            else:
                pip_cmd = "pip"
            logger.warning(
                "You are using pip version %s, however version %s is "
                "available.\nYou should consider upgrading via the "
                "'%s install --upgrade pip' command.",
                pip_version, pypi_version, pip_cmd
            )
    except Exception:
        logger.debug(
            "There was an error checking the latest version of pip",
            exc_info=True,
        )