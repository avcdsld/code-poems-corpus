def clean_requires_python(candidates):
    """Get a cleaned list of all the candidates with valid specifiers in the `requires_python` attributes."""
    all_candidates = []
    sys_version = ".".join(map(str, sys.version_info[:3]))
    from packaging.version import parse as parse_version

    py_version = parse_version(os.environ.get("PIP_PYTHON_VERSION", sys_version))
    for c in candidates:
        from_location = attrgetter("location.requires_python")
        requires_python = getattr(c, "requires_python", from_location(c))
        if requires_python:
            # Old specifications had people setting this to single digits
            # which is effectively the same as '>=digit,<digit+1'
            if requires_python.isdigit():
                requires_python = ">={0},<{1}".format(
                    requires_python, int(requires_python) + 1
                )
            try:
                specifierset = SpecifierSet(requires_python)
            except InvalidSpecifier:
                continue
            else:
                if not specifierset.contains(py_version):
                    continue
        all_candidates.append(c)
    return all_candidates