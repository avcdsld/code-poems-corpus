def create_handler_venv(self):
        """
        Takes the installed zappa and brings it into a fresh virtualenv-like folder. All dependencies are then downloaded.
        """
        import subprocess

        # We will need the currenv venv to pull Zappa from
        current_venv = self.get_current_venv()

        # Make a new folder for the handler packages
        ve_path = os.path.join(os.getcwd(), 'handler_venv')

        if os.sys.platform == 'win32':
            current_site_packages_dir = os.path.join(current_venv, 'Lib', 'site-packages')
            venv_site_packages_dir = os.path.join(ve_path, 'Lib', 'site-packages')
        else:
            current_site_packages_dir = os.path.join(current_venv, 'lib', get_venv_from_python_version(), 'site-packages')
            venv_site_packages_dir = os.path.join(ve_path, 'lib', get_venv_from_python_version(), 'site-packages')

        if not os.path.isdir(venv_site_packages_dir):
            os.makedirs(venv_site_packages_dir)

        # Copy zappa* to the new virtualenv
        zappa_things = [z for z in os.listdir(current_site_packages_dir) if z.lower()[:5] == 'zappa']
        for z in zappa_things:
            copytree(os.path.join(current_site_packages_dir, z), os.path.join(venv_site_packages_dir, z))

        # Use pip to download zappa's dependencies. Copying from current venv causes issues with things like PyYAML that installs as yaml
        zappa_deps = self.get_deps_list('zappa')
        pkg_list = ['{0!s}=={1!s}'.format(dep, version) for dep, version in zappa_deps]

        # Need to manually add setuptools
        pkg_list.append('setuptools')
        command = ["pip", "install", "--quiet", "--target", venv_site_packages_dir] + pkg_list

        # This is the recommended method for installing packages if you don't
        # to depend on `setuptools`
        # https://github.com/pypa/pip/issues/5240#issuecomment-381662679
        pip_process = subprocess.Popen(command, stdout=subprocess.PIPE)
        # Using communicate() to avoid deadlocks
        pip_process.communicate()
        pip_return_code = pip_process.returncode

        if pip_return_code:
          raise EnvironmentError("Pypi lookup failed")

        return ve_path