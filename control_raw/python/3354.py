def merge(self, other):
        """Extend the annotations of this binder with the annotations from another."""
        assert self.attrs == other.attrs
        self.tokens.extend(other.tokens)
        self.spaces.extend(other.spaces)
        self.strings.update(other.strings)