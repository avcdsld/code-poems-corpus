def validate_multiindex(self, obj):
        """validate that we can store the multi-index; reset and return the
        new object
        """
        levels = [l if l is not None else "level_{0}".format(i)
                  for i, l in enumerate(obj.index.names)]
        try:
            return obj.reset_index(), levels
        except ValueError:
            raise ValueError("duplicate names/columns in the multi-index when "
                             "storing as a table")