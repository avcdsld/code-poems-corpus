def _copy_new_parent(self, parent):
        """Copy the current param to a new parent, must be a dummy param."""
        if self.parent == "undefined":
            param = copy.copy(self)
            param.parent = parent.uid
            return param
        else:
            raise ValueError("Cannot copy from non-dummy parent %s." % parent)