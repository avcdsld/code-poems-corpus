def select(self, key, where=None, start=None, stop=None, columns=None,
               iterator=False, chunksize=None, auto_close=False, **kwargs):
        """
        Retrieve pandas object stored in file, optionally based on where
        criteria

        Parameters
        ----------
        key : object
        where : list of Term (or convertible) objects, optional
        start : integer (defaults to None), row number to start selection
        stop  : integer (defaults to None), row number to stop selection
        columns : a list of columns that if not None, will limit the return
            columns
        iterator : boolean, return an iterator, default False
        chunksize : nrows to include in iteration, return an iterator
        auto_close : boolean, should automatically close the store when
            finished, default is False

        Returns
        -------
        The selected object
        """
        group = self.get_node(key)
        if group is None:
            raise KeyError('No object named {key} in the file'.format(key=key))

        # create the storer and axes
        where = _ensure_term(where, scope_level=1)
        s = self._create_storer(group)
        s.infer_axes()

        # function to call on iteration
        def func(_start, _stop, _where):
            return s.read(start=_start, stop=_stop,
                          where=_where,
                          columns=columns)

        # create the iterator
        it = TableIterator(self, s, func, where=where, nrows=s.nrows,
                           start=start, stop=stop, iterator=iterator,
                           chunksize=chunksize, auto_close=auto_close)

        return it.get_result()