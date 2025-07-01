def run (self, project, name, prop_set, sources):
        """ Tries to invoke this generator on the given sources. Returns a
            list of generated targets (instances of 'virtual-target').

            project:        Project for which the targets are generated.

            name:           Determines the name of 'name' attribute for
                            all generated targets. See 'generated_targets' method.

            prop_set:       Desired properties for generated targets.

            sources:        Source targets.
        """
        if __debug__:
            from .targets import ProjectTarget
            assert isinstance(project, ProjectTarget)
            # intermediary targets don't have names, so None is possible
            assert isinstance(name, basestring) or name is None
            assert isinstance(prop_set, property_set.PropertySet)
            assert is_iterable_typed(sources, virtual_target.VirtualTarget)
        if project.manager ().logger ().on ():
            project.manager ().logger ().log (__name__, "  generator '%s'" % self.id_)
            project.manager ().logger ().log (__name__, "  composing: '%s'" % self.composing_)

        if not sources:
            s = 'An empty source list was passed in to the "{}" generator'.format(self.id_)
            if name:
                s += ' for target "{}"'.format(name)
            raise InvalidTargetSource(s)

        if not self.composing_ and len (sources) > 1 and len (self.source_types_) > 1:
            raise BaseException ("Unsupported source/source_type combination")

        # We don't run composing generators if no name is specified. The reason
        # is that composing generator combines several targets, which can have
        # different names, and it cannot decide which name to give for produced
        # target. Therefore, the name must be passed.
        #
        # This in effect, means that composing generators are runnable only
        # at top-level of transofrmation graph, or if name is passed explicitly.
        # Thus, we dissallow composing generators in the middle. For example, the
        # transofrmation CPP -> OBJ -> STATIC_LIB -> RSP -> EXE won't be allowed
        # (the OBJ -> STATIC_LIB generator is composing)
        if not self.composing_ or name:
            return self.run_really (project, name, prop_set, sources)
        else:
            return []