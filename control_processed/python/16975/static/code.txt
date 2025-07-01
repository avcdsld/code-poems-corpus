def compute_usage_requirements (self, subvariant):
        """ Given the set of generated targets, and refined build
            properties, determines and sets appripriate usage requirements
            on those targets.
        """
        assert isinstance(subvariant, virtual_target.Subvariant)
        rproperties = subvariant.build_properties ()
        xusage_requirements =self.evaluate_requirements(
            self.usage_requirements_, rproperties, "added")

        # We generate all dependency properties and add them,
        # as well as their usage requirements, to result.
        (r1, r2) = self.generate_dependency_properties(xusage_requirements.dependency (), rproperties)
        extra = r1 + r2

        result = property_set.create (xusage_requirements.non_dependency () + extra)

        # Propagate usage requirements we've got from sources, except
        # for the <pch-header> and <pch-file> features.
        #
        # That feature specifies which pch file to use, and should apply
        # only to direct dependents. Consider:
        #
        #   pch pch1 : ...
        #   lib lib1 : ..... pch1 ;
        #   pch pch2 :
        #   lib lib2 : pch2 lib1 ;
        #
        # Here, lib2 should not get <pch-header> property from pch1.
        #
        # Essentially, when those two features are in usage requirements,
        # they are propagated only to direct dependents. We might need
        # a more general mechanism, but for now, only those two
        # features are special.
        properties = []
        for p in subvariant.sources_usage_requirements().all():
            if p.feature.name not in ('pch-header', 'pch-file'):
                properties.append(p)
        if 'shared' in rproperties.get('link'):
            new_properties = []
            for p in properties:
                if p.feature.name != 'library':
                    new_properties.append(p)
            properties = new_properties

        result = result.add_raw(properties)
        return result