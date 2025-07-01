def write_data_chunk(self, rows, indexes, mask, values):
        """
        Parameters
        ----------
        rows : an empty memory space where we are putting the chunk
        indexes : an array of the indexes
        mask : an array of the masks
        values : an array of the values
        """

        # 0 len
        for v in values:
            if not np.prod(v.shape):
                return

        try:
            nrows = indexes[0].shape[0]
            if nrows != len(rows):
                rows = np.empty(nrows, dtype=self.dtype)
            names = self.dtype.names
            nindexes = len(indexes)

            # indexes
            for i, idx in enumerate(indexes):
                rows[names[i]] = idx

            # values
            for i, v in enumerate(values):
                rows[names[i + nindexes]] = v

            # mask
            if mask is not None:
                m = ~mask.ravel().astype(bool, copy=False)
                if not m.all():
                    rows = rows[m]

        except Exception as detail:
            raise Exception(
                "cannot create row-data -> {detail}".format(detail=detail))

        try:
            if len(rows):
                self.table.append(rows)
                self.table.flush()
        except Exception as detail:
            raise TypeError(
                "tables cannot write this data -> {detail}".format(
                    detail=detail))