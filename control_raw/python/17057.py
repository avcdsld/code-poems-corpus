def append(self, other):
        """
        Append an SArray to the current SArray. Creates a new SArray with the
        rows from both SArrays. Both SArrays must be of the same type.

        Parameters
        ----------
        other : SArray
            Another SArray whose rows are appended to current SArray.

        Returns
        -------
        out : SArray
            A new SArray that contains rows from both SArrays, with rows from
            the ``other`` SArray coming after all rows from the current SArray.

        See Also
        --------
        SFrame.append

        Examples
        --------
        >>> sa = turicreate.SArray([1, 2, 3])
        >>> sa2 = turicreate.SArray([4, 5, 6])
        >>> sa.append(sa2)
        dtype: int
        Rows: 6
        [1, 2, 3, 4, 5, 6]
        """
        if type(other) is not SArray:
            raise RuntimeError("SArray append can only work with SArray")

        if self.dtype != other.dtype:
            raise RuntimeError("Data types in both SArrays have to be the same")

        with cython_context():
            return SArray(_proxy = self.__proxy__.append(other.__proxy__))