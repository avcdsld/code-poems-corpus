def package(
        self, name, version, extras=None
    ):  # type: (...) -> poetry.packages.Package
        """
        Retrieve the release information.

        This is a heavy task which takes time.
        We have to download a package to get the dependencies.
        We also need to download every file matching this release
        to get the various hashes.

        Note that, this will be cached so the subsequent operations
        should be much faster.
        """
        try:
            index = self._packages.index(
                poetry.packages.Package(name, version, version)
            )

            return self._packages[index]
        except ValueError:
            if extras is None:
                extras = []

            release_info = self.get_release_info(name, version)

            package = poetry.packages.Package(name, version, version)
            if release_info["requires_python"]:
                package.python_versions = release_info["requires_python"]

            package.source_type = "legacy"
            package.source_url = self._url
            package.source_reference = self.name

            requires_dist = release_info["requires_dist"] or []
            for req in requires_dist:
                try:
                    dependency = dependency_from_pep_508(req)
                except InvalidMarker:
                    # Invalid marker
                    # We strip the markers hoping for the best
                    req = req.split(";")[0]

                    dependency = dependency_from_pep_508(req)
                except ValueError:
                    # Likely unable to parse constraint so we skip it
                    self._log(
                        "Invalid constraint ({}) found in {}-{} dependencies, "
                        "skipping".format(req, package.name, package.version),
                        level="debug",
                    )
                    continue

                if dependency.in_extras:
                    for extra in dependency.in_extras:
                        if extra not in package.extras:
                            package.extras[extra] = []

                        package.extras[extra].append(dependency)

                if not dependency.is_optional():
                    package.requires.append(dependency)

            # Adding description
            package.description = release_info.get("summary", "")

            # Adding hashes information
            package.hashes = release_info["digests"]

            # Activate extra dependencies
            for extra in extras:
                if extra in package.extras:
                    for dep in package.extras[extra]:
                        dep.activate()

                    package.requires += package.extras[extra]

            self._packages.append(package)

            return package