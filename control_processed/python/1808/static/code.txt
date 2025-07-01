def get_atom_coltype(self, kind=None):
        """ return the PyTables column class for this column """
        if kind is None:
            kind = self.kind
        if self.kind.startswith('uint'):
            col_name = "UInt{name}Col".format(name=kind[4:])
        else:
            col_name = "{name}Col".format(name=kind.capitalize())

        return getattr(_tables(), col_name)