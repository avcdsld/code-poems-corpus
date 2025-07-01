def close(self):
        """
        When a client closes a file, this method is called on the handle.
        Normally you would use this method to close the underlying OS level
        file object(s).

        The default implementation checks for attributes on ``self`` named
        ``readfile`` and/or ``writefile``, and if either or both are present,
        their ``close()`` methods are called.  This means that if you are
        using the default implementations of `read` and `write`, this
        method's default implementation should be fine also.
        """
        readfile = getattr(self, "readfile", None)
        if readfile is not None:
            readfile.close()
        writefile = getattr(self, "writefile", None)
        if writefile is not None:
            writefile.close()