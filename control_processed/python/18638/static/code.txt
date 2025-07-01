def add(self, data, name=None):
        ''' Appends a new column of data to the data source.

        Args:
            data (seq) : new data to add
            name (str, optional) : column name to use.
                If not supplied, generate a name of the form "Series ####"

        Returns:
            str:  the column name used

        '''
        if name is None:
            n = len(self.data)
            while "Series %d"%n in self.data:
                n += 1
            name = "Series %d"%n
        self.data[name] = data
        return name