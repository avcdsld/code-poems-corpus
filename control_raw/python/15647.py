def init(version = None, command = None, options = None):
    """
        Initializes the gcc toolset for the given version. If necessary, command may
        be used to specify where the compiler is located. The parameter 'options' is a
        space-delimited list of options, each one specified as
        <option-name>option-value. Valid option names are: cxxflags, linkflags and
        linker-type. Accepted linker-type values are gnu, darwin, osf, hpux or sun
        and the default value will be selected based on the current OS.
        Example:
          using gcc : 3.4 : : <cxxflags>foo <linkflags>bar <linker-type>sun ;
    """

    options = to_seq(options)
    command = to_seq(command)

    # Information about the gcc command...
    #   The command.
    command = to_seq(common.get_invocation_command('gcc', 'g++', command))
    #   The root directory of the tool install.
    root = feature.get_values('<root>', options)
    root = root[0] if root else ''
    #   The bin directory where to find the command to execute.
    bin = None
    #   The flavor of compiler.
    flavor = feature.get_values('<flavor>', options)
    flavor = flavor[0] if flavor else ''
    #   Autodetect the root and bin dir if not given.
    if command:
        if not bin:
            bin = common.get_absolute_tool_path(command[-1])
        if not root:
            root = os.path.dirname(bin)
    #   Autodetect the version and flavor if not given.
    if command:
        machine_info = subprocess.Popen(command + ['-dumpmachine'], stdout=subprocess.PIPE).communicate()[0]
        machine = __machine_match.search(machine_info).group(1)

        version_info = subprocess.Popen(command + ['-dumpversion'], stdout=subprocess.PIPE).communicate()[0]
        version = __version_match.search(version_info).group(1)
        if not flavor and machine.find('mingw') != -1:
            flavor = 'mingw'

    condition = None
    if flavor:
        condition = common.check_init_parameters('gcc', None,
            ('version', version),
            ('flavor', flavor))
    else:
        condition = common.check_init_parameters('gcc', None,
            ('version', version))

    if command:
        command = command[0]

    common.handle_options('gcc', condition, command, options)

    linker = feature.get_values('<linker-type>', options)
    if not linker:
        if os_name() == 'OSF':
            linker = 'osf'
        elif os_name() == 'HPUX':
            linker = 'hpux' ;
        else:
            linker = 'gnu'

    init_link_flags('gcc', linker, condition)

    # If gcc is installed in non-standard location, we'd need to add
    # LD_LIBRARY_PATH when running programs created with it (for unit-test/run
    # rules).
    if command:
        # On multilib 64-bit boxes, there are both 32-bit and 64-bit libraries
        # and all must be added to LD_LIBRARY_PATH. The linker will pick the
        # right onces. Note that we don't provide a clean way to build 32-bit
        # binary with 64-bit compiler, but user can always pass -m32 manually.
        lib_path = [os.path.join(root, 'bin'),
                    os.path.join(root, 'lib'),
                    os.path.join(root, 'lib32'),
                    os.path.join(root, 'lib64')]
        if debug():
            print 'notice: using gcc libraries ::', condition, '::', lib_path
        toolset.flags('gcc.link', 'RUN_PATH', condition, lib_path)

    # If it's not a system gcc install we should adjust the various programs as
    # needed to prefer using the install specific versions. This is essential
    # for correct use of MinGW and for cross-compiling.

    # - The archive builder.
    archiver = common.get_invocation_command('gcc',
            'ar', feature.get_values('<archiver>', options), [bin], path_last=True)
    toolset.flags('gcc.archive', '.AR', condition, [archiver])
    if debug():
        print 'notice: using gcc archiver ::', condition, '::', archiver

    # - Ranlib
    ranlib = common.get_invocation_command('gcc',
            'ranlib', feature.get_values('<ranlib>', options), [bin], path_last=True)
    toolset.flags('gcc.archive', '.RANLIB', condition, [ranlib])
    if debug():
        print 'notice: using gcc archiver ::', condition, '::', ranlib

    # - The resource compiler.
    rc_command = common.get_invocation_command_nodefault('gcc',
            'windres', feature.get_values('<rc>', options), [bin], path_last=True)
    rc_type = feature.get_values('<rc-type>', options)

    if not rc_type:
        rc_type = 'windres'

    if not rc_command:
        # If we can't find an RC compiler we fallback to a null RC compiler that
        # creates empty object files. This allows the same Jamfiles to work
        # across the board. The null RC uses the assembler to create the empty
        # objects, so configure that.
        rc_command = common.get_invocation_command('gcc', 'as', [], [bin], path_last=True)
        rc_type = 'null'
    rc.configure([rc_command], condition, ['<rc-type>' + rc_type])