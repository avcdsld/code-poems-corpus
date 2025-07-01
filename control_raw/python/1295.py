def conda_package_to_pip(package):
    """
    Convert a conda package to its pip equivalent.

    In most cases they are the same, those are the exceptions:
    - Packages that should be excluded (in `EXCLUDE`)
    - Packages that should be renamed (in `RENAME`)
    - A package requiring a specific version, in conda is defined with a single
      equal (e.g. ``pandas=1.0``) and in pip with two (e.g. ``pandas==1.0``)
    """
    if package in EXCLUDE:
        return

    package = re.sub('(?<=[^<>])=', '==', package).strip()
    for compare in ('<=', '>=', '=='):
        if compare not in package:
            continue

        pkg, version = package.split(compare)

        if pkg in RENAME:
            return ''.join((RENAME[pkg], compare, version))

        break

    return package