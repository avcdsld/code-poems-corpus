def matches_requirement(self, req):
        """
        Say if this instance matches (fulfills) a requirement.
        :param req: The requirement to match.
        :rtype req: str
        :return: True if it matches, else False.
        """
        # Requirement may contain extras - parse to lose those
        # from what's passed to the matcher
        r = parse_requirement(req)
        scheme = get_scheme(self.metadata.scheme)
        try:
            matcher = scheme.matcher(r.requirement)
        except UnsupportedVersionError:
            # XXX compat-mode if cannot read the version
            logger.warning('could not read version %r - using name only',
                           req)
            name = req.split()[0]
            matcher = scheme.matcher(name)

        name = matcher.key   # case-insensitive

        result = False
        for p in self.provides:
            p_name, p_ver = parse_name_and_version(p)
            if p_name != name:
                continue
            try:
                result = matcher.match(p_ver)
                break
            except UnsupportedVersionError:
                pass
        return result