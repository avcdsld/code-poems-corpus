def profile(self, new_profile):
        """Sets location of the browser profile to use, either by string
        or ``FirefoxProfile``.

        """
        if not isinstance(new_profile, FirefoxProfile):
            new_profile = FirefoxProfile(new_profile)
        self._profile = new_profile