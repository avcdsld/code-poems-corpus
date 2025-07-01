def check_requirements(self, reqs):
        # type: (Iterable[str]) -> Tuple[Set[Tuple[str, str]], Set[str]]
        """Return 2 sets:
            - conflicting requirements: set of (installed, wanted) reqs tuples
            - missing requirements: set of reqs
        """
        missing = set()
        conflicting = set()
        if reqs:
            ws = WorkingSet(self._lib_dirs)
            for req in reqs:
                try:
                    if ws.find(Requirement.parse(req)) is None:
                        missing.add(req)
                except VersionConflict as e:
                    conflicting.add((str(e.args[0].as_requirement()),
                                     str(e.args[1])))
        return conflicting, missing