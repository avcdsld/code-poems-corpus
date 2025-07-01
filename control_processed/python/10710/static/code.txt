def get_adjusted_value(self, asset, field, dt,
                           perspective_dt,
                           data_frequency,
                           spot_value=None):
        """
        Returns a scalar value representing the value
        of the desired asset's field at the given dt with adjustments applied.

        Parameters
        ----------
        asset : Asset
            The asset whose data is desired.
        field : {'open', 'high', 'low', 'close', 'volume', \
                 'price', 'last_traded'}
            The desired field of the asset.
        dt : pd.Timestamp
            The timestamp for the desired value.
        perspective_dt : pd.Timestamp
            The timestamp from which the data is being viewed back from.
        data_frequency : str
            The frequency of the data to query; i.e. whether the data is
            'daily' or 'minute' bars

        Returns
        -------
        value : float, int, or pd.Timestamp
            The value of the given ``field`` for ``asset`` at ``dt`` with any
            adjustments known by ``perspective_dt`` applied. The return type is
            based on the ``field`` requested. If the field is one of 'open',
            'high', 'low', 'close', or 'price', the value will be a float. If
            the ``field`` is 'volume' the value will be a int. If the ``field``
            is 'last_traded' the value will be a Timestamp.
        """
        if spot_value is None:
            # if this a fetcher field, we want to use perspective_dt (not dt)
            # because we want the new value as of midnight (fetcher only works
            # on a daily basis, all timestamps are on midnight)
            if self._is_extra_source(asset, field,
                                     self._augmented_sources_map):
                spot_value = self.get_spot_value(asset, field, perspective_dt,
                                                 data_frequency)
            else:
                spot_value = self.get_spot_value(asset, field, dt,
                                                 data_frequency)

        if isinstance(asset, Equity):
            ratio = self.get_adjustments(asset, field, dt, perspective_dt)[0]
            spot_value *= ratio

        return spot_value