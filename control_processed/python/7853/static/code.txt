def var(self):
        """Returns a symbol representing this parameter."""
        if self._var is None:
            self._var = symbol.var(self.name, shape=self.shape, dtype=self.dtype,
                                   lr_mult=self.lr_mult, wd_mult=self.wd_mult,
                                   init=self.init, stype=self._stype)
        return self._var