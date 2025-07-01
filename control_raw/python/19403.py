def is_python_interpreter(filename):
    """Evaluate wether a file is a python interpreter or not."""
    real_filename = os.path.realpath(filename)  # To follow symlink if existent
    if (not osp.isfile(real_filename) or 
        not is_python_interpreter_valid_name(filename)):
        return False
    elif is_pythonw(filename):
        if os.name == 'nt':
            # pythonw is a binary on Windows
            if not encoding.is_text_file(real_filename):
                return True
            else:
                return False
        elif sys.platform == 'darwin':
            # pythonw is a text file in Anaconda but a binary in
            # the system
            if is_anaconda() and encoding.is_text_file(real_filename):
                return True
            elif not encoding.is_text_file(real_filename):
                return True
            else:
                return False
        else:
            # There's no pythonw in other systems
            return False
    elif encoding.is_text_file(real_filename):
        # At this point we can't have a text file
        return False
    else:
        return check_python_help(filename)