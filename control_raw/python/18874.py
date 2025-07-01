def _axis(self, axis):
        """
        Return the corresponding labels taking into account the axis.

        The axis could be horizontal (0) or vertical (1).
        """
        return self.df.columns if axis == 0 else self.df.index