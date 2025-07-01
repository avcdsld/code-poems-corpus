def get_attr(self):
        """ get the data for this column """
        self.values = getattr(self.attrs, self.kind_attr, None)
        self.dtype = getattr(self.attrs, self.dtype_attr, None)
        self.meta = getattr(self.attrs, self.meta_attr, None)
        self.set_kind()