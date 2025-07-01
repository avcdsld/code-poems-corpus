def get_finder(sources=None, pip_command=None, pip_options=None):
    # type: (List[Dict[S, Union[S, bool]]], Optional[Command], Any) -> PackageFinder
    """Get a package finder for looking up candidates to install

    :param sources: A list of pipfile-formatted sources, defaults to None
    :param sources: list[dict], optional
    :param pip_command: A pip command instance, defaults to None
    :type pip_command: :class:`~pip._internal.cli.base_command.Command`
    :param pip_options: A pip options, defaults to None
    :type pip_options: :class:`~pip._internal.cli.cmdoptions`
    :return: A package finder
    :rtype: :class:`~pip._internal.index.PackageFinder`
    """

    if not pip_command:
        pip_command = get_pip_command()
    if not sources:
        sources = [
            {"url": "https://pypi.org/simple", "name": "pypi", "verify_ssl": True}
        ]
    if not pip_options:
        pip_options = get_pip_options(sources=sources, pip_command=pip_command)
    session = pip_command._build_session(pip_options)
    atexit.register(session.close)
    finder = pip_shims.shims.PackageFinder(
        find_links=[],
        index_urls=[s.get("url") for s in sources],
        trusted_hosts=[],
        allow_all_prereleases=pip_options.pre,
        session=session,
    )
    return finder