def _compute_dependencies(self):
        """Recompute this distribution's dependencies."""
        dm = self.__dep_map = {None: []}

        reqs = []
        # Including any condition expressions
        for req in self._parsed_pkg_info.get_all('Requires-Dist') or []:
            reqs.extend(parse_requirements(req))

        def reqs_for_extra(extra):
            for req in reqs:
                if not req.marker or req.marker.evaluate({'extra': extra}):
                    yield req

        common = frozenset(reqs_for_extra(None))
        dm[None].extend(common)

        for extra in self._parsed_pkg_info.get_all('Provides-Extra') or []:
            s_extra = safe_extra(extra.strip())
            dm[s_extra] = list(frozenset(reqs_for_extra(extra)) - common)

        return dm