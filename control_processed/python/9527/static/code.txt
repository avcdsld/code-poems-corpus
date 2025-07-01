def is_pinned(self):
        # type: () -> bool
        """Return whether I am pinned to an exact version.

        For example, some-package==1.2 is pinned; some-package>1.2 is not.
        """
        specifiers = self.specifier
        return (len(specifiers) == 1 and
                next(iter(specifiers)).operator in {'==', '==='})