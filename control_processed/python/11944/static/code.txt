def is_subset(self, other):
        """Returns True if self has the same or fewer permissions as other."""
        if isinstance(other, Permissions):
            return (self.value & other.value) == self.value
        else:
            raise TypeError("cannot compare {} with {}".format(self.__class__.__name__, other.__class__.__name__))