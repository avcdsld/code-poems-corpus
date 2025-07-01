def _get_pypirc_command(self):
        """
        Get the distutils command for interacting with PyPI configurations.
        :return: the command.
        """
        from distutils.core import Distribution
        from distutils.config import PyPIRCCommand
        d = Distribution()
        return PyPIRCCommand(d)