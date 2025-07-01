def _reverse_dependencies(self, cache_keys):
        """
        Returns a lookup table of reverse dependencies for all the given cache keys.

        Example input:

            [('pep8', '1.5.7'),
             ('flake8', '2.4.0'),
             ('mccabe', '0.3'),
             ('pyflakes', '0.8.1')]

        Example output:

            {'pep8': ['flake8'],
             'flake8': [],
             'mccabe': ['flake8'],
             'pyflakes': ['flake8']}

        """
        # First, collect all the dependencies into a sequence of (parent, child) tuples, like [('flake8', 'pep8'),
        # ('flake8', 'mccabe'), ...]
        return lookup_table((key_from_req(Requirement(dep_name)), name)
                            for name, version_and_extras in cache_keys
                            for dep_name in self.cache[name][version_and_extras])