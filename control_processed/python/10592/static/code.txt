def handle_market_close(self, dt, data_portal):
        """Handles the close of the given day.

        Parameters
        ----------
        dt : Timestamp
            The most recently completed simulation datetime.
        data_portal : DataPortal
            The current data portal.

        Returns
        -------
        A daily perf packet.
        """
        completed_session = self._current_session

        if self.emission_rate == 'daily':
            # this method is called for both minutely and daily emissions, but
            # this chunk of code here only applies for daily emissions. (since
            # it's done every minute, elsewhere, for minutely emission).
            self.sync_last_sale_prices(dt, data_portal)

        session_ix = self._session_count
        # increment the day counter before we move markers forward.
        self._session_count += 1

        packet = {
            'period_start': self._first_session,
            'period_end': self._last_session,
            'capital_base': self._capital_base,
            'daily_perf': {
                'period_open': self._market_open,
                'period_close': dt,
            },
            'cumulative_perf': {
                'period_open': self._first_session,
                'period_close': self._last_session,
            },
            'progress': self._progress(self),
            'cumulative_risk_metrics': {},
        }
        ledger = self._ledger
        ledger.end_of_session(session_ix)
        self.end_of_session(
            packet,
            ledger,
            completed_session,
            session_ix,
            data_portal,
        )

        return packet