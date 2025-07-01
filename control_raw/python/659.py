def toListString(value):
        """
        Convert a value to list of strings, if possible.
        """
        if TypeConverters._can_convert_to_list(value):
            value = TypeConverters.toList(value)
            if all(map(lambda v: TypeConverters._can_convert_to_string(v), value)):
                return [TypeConverters.toString(v) for v in value]
        raise TypeError("Could not convert %s to list of strings" % value)