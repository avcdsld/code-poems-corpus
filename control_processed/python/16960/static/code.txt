def mark_targets_as_explicit (self, target_names):
        """Add 'target' to the list of targets in this project
        that should be build only by explicit request."""

        # Record the name of the target, not instance, since this
        # rule is called before main target instaces are created.
        assert is_iterable_typed(target_names, basestring)
        self.explicit_targets_.update(target_names)