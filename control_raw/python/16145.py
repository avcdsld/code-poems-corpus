def clone_and_change_target_type(self, base, type):
        """Creates another generator that is the same as $(self), except that
        if 'base' is in target types of $(self), 'type' will in target types
        of the new generator."""
        assert isinstance(base, basestring)
        assert isinstance(type, basestring)
        target_types = []
        for t in self.target_types_and_names_:
            m = _re_match_type.match(t)
            assert m

            if m.group(1) == base:
                if m.group(2):
                    target_types.append(type + m.group(2))
                else:
                    target_types.append(type)
            else:
                target_types.append(t)

        return self.__class__(self.id_, self.composing_,
                              self.source_types_,
                              target_types,
                              self.requirements_)