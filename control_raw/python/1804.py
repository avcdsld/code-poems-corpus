def convert(self, values, nan_rep, encoding, errors):
        """ set the values from this selection: take = take ownership """

        self.values = Int64Index(np.arange(self.table.nrows))
        return self