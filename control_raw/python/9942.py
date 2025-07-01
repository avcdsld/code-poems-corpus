def _normalized_keys(self, section, items):
        # type: (str, Iterable[Tuple[str, Any]]) -> Dict[str, Any]
        """Normalizes items to construct a dictionary with normalized keys.

        This routine is where the names become keys and are made the same
        regardless of source - configuration files or environment.
        """
        normalized = {}
        for name, val in items:
            key = section + "." + _normalize_name(name)
            normalized[key] = val
        return normalized