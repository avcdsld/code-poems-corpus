def split_by_list(self, train, valid):
        "Split the data between `train` and `valid`."
        return self._split(self.path, train, valid)