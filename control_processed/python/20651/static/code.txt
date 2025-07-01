def parse(self, val):
        """
        Parses a ``bool`` from the string, matching 'true' or 'false' ignoring case.
        """
        s = str(val).lower()
        if s == "true":
            return True
        elif s == "false":
            return False
        else:
            raise ValueError("cannot interpret '{}' as boolean".format(val))