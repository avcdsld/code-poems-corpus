def build(args) -> None:
    """Build using CMake"""
    venv_exe = shutil.which('virtualenv')
    pyexe = shutil.which(args.pyexe)
    if not venv_exe:
        logging.warn("virtualenv wasn't found in path, it's recommended to install virtualenv to manage python environments")
    if not pyexe:
        logging.warn("Python executable %s not found in path", args.pyexe)
    if args.cmake_options:
        cmake = CMake(args.cmake_options)
    else:
        cmake = CMake()
    cmake()
    create_virtualenv(venv_exe, pyexe, args.venv)