def get_loc_level(self, key, level=0, drop_level=True):
        """
        Get both the location for the requested label(s) and the
        resulting sliced index.

        Parameters
        ----------
        key : label or sequence of labels
        level : int/level name or list thereof, optional
        drop_level : bool, default True
            if ``False``, the resulting index will not drop any level.

        Returns
        -------
        loc : A 2-tuple where the elements are:
              Element 0: int, slice object or boolean array
              Element 1: The resulting sliced multiindex/index. If the key
              contains all levels, this will be ``None``.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([list('abb'), list('def')],
        ...                                names=['A', 'B'])

        >>> mi.get_loc_level('b')
        (slice(1, 3, None), Index(['e', 'f'], dtype='object', name='B'))

        >>> mi.get_loc_level('e', level='B')
        (array([False,  True, False], dtype=bool),
        Index(['b'], dtype='object', name='A'))

        >>> mi.get_loc_level(['b', 'e'])
        (1, None)

        See Also
        ---------
        MultiIndex.get_loc  : Get location for a label or a tuple of labels.
        MultiIndex.get_locs : Get location for a label/slice/list/mask or a
                              sequence of such.
        """

        def maybe_droplevels(indexer, levels, drop_level):
            if not drop_level:
                return self[indexer]
            # kludgearound
            orig_index = new_index = self[indexer]
            levels = [self._get_level_number(i) for i in levels]
            for i in sorted(levels, reverse=True):
                try:
                    new_index = new_index.droplevel(i)
                except ValueError:

                    # no dropping here
                    return orig_index
            return new_index

        if isinstance(level, (tuple, list)):
            if len(key) != len(level):
                raise AssertionError('Key for location must have same '
                                     'length as number of levels')
            result = None
            for lev, k in zip(level, key):
                loc, new_index = self.get_loc_level(k, level=lev)
                if isinstance(loc, slice):
                    mask = np.zeros(len(self), dtype=bool)
                    mask[loc] = True
                    loc = mask

                result = loc if result is None else result & loc

            return result, maybe_droplevels(result, level, drop_level)

        level = self._get_level_number(level)

        # kludge for #1796
        if isinstance(key, list):
            key = tuple(key)

        if isinstance(key, tuple) and level == 0:

            try:
                if key in self.levels[0]:
                    indexer = self._get_level_indexer(key, level=level)
                    new_index = maybe_droplevels(indexer, [0], drop_level)
                    return indexer, new_index
            except TypeError:
                pass

            if not any(isinstance(k, slice) for k in key):

                # partial selection
                # optionally get indexer to avoid re-calculation
                def partial_selection(key, indexer=None):
                    if indexer is None:
                        indexer = self.get_loc(key)
                    ilevels = [i for i in range(len(key))
                               if key[i] != slice(None, None)]
                    return indexer, maybe_droplevels(indexer, ilevels,
                                                     drop_level)

                if len(key) == self.nlevels and self.is_unique:
                    # Complete key in unique index -> standard get_loc
                    return (self._engine.get_loc(key), None)
                else:
                    return partial_selection(key)
            else:
                indexer = None
                for i, k in enumerate(key):
                    if not isinstance(k, slice):
                        k = self._get_level_indexer(k, level=i)
                        if isinstance(k, slice):
                            # everything
                            if k.start == 0 and k.stop == len(self):
                                k = slice(None, None)
                        else:
                            k_index = k

                    if isinstance(k, slice):
                        if k == slice(None, None):
                            continue
                        else:
                            raise TypeError(key)

                    if indexer is None:
                        indexer = k_index
                    else:  # pragma: no cover
                        indexer &= k_index
                if indexer is None:
                    indexer = slice(None, None)
                ilevels = [i for i in range(len(key))
                           if key[i] != slice(None, None)]
                return indexer, maybe_droplevels(indexer, ilevels, drop_level)
        else:
            indexer = self._get_level_indexer(key, level=level)
            return indexer, maybe_droplevels(indexer, [level], drop_level)