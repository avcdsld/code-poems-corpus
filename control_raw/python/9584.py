def is_installable_dir(path):
    # type: (str) -> bool
    """Is path is a directory containing setup.py or pyproject.toml?
    """
    if not os.path.isdir(path):
        return False
    setup_py = os.path.join(path, 'setup.py')
    if os.path.isfile(setup_py):
        return True
    pyproject_toml = os.path.join(path, 'pyproject.toml')
    if os.path.isfile(pyproject_toml):
        return True
    return False