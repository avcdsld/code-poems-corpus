def wrap(cls, value):
        ''' Some property types need to wrap their values in special containers, etc.

        '''
        if isinstance(value, dict):
            if isinstance(value, PropertyValueDict):
                return value
            else:
                return PropertyValueDict(value)
        else:
            return value