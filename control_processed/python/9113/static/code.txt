def get_legacy_build_wheel_path(
    names,  # type: List[str]
    temp_dir,  # type: str
    req,  # type: InstallRequirement
    command_args,  # type: List[str]
    command_output,  # type: str
):
    # type: (...) -> Optional[str]
    """
    Return the path to the wheel in the temporary build directory.
    """
    # Sort for determinism.
    names = sorted(names)
    if not names:
        msg = (
            'Legacy build of wheel for {!r} created no files.\n'
        ).format(req.name)
        msg += format_command(command_args, command_output)
        logger.warning(msg)
        return None

    if len(names) > 1:
        msg = (
            'Legacy build of wheel for {!r} created more than one file.\n'
            'Filenames (choosing first): {}\n'
        ).format(req.name, names)
        msg += format_command(command_args, command_output)
        logger.warning(msg)

    return os.path.join(temp_dir, names[0])