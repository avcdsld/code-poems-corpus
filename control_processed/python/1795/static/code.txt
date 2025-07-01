def is_indexed(self):
        """ return whether I am an indexed column """
        try:
            return getattr(self.table.cols, self.cname).is_indexed
        except AttributeError:
            False