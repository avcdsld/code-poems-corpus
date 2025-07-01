def roll_forward(self, dt):
        """
        Given a date, align it to the calendar of the pipeline's domain.

        Parameters
        ----------
        dt : pd.Timestamp

        Returns
        -------
        pd.Timestamp
        """
        dt = pd.Timestamp(dt, tz='UTC')

        trading_days = self.all_sessions()
        try:
            return trading_days[trading_days.searchsorted(dt)]
        except IndexError:
            raise ValueError(
                "Date {} was past the last session for domain {}. "
                "The last session for this domain is {}.".format(
                    dt.date(),
                    self,
                    trading_days[-1].date()
                )
            )