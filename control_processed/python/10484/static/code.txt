def _get_minute_message(self, dt, algo, metrics_tracker):
        """
        Get a perf message for the given datetime.
        """
        rvars = algo.recorded_vars

        minute_message = metrics_tracker.handle_minute_close(
            dt,
            self.data_portal,
        )

        minute_message['minute_perf']['recorded_vars'] = rvars
        return minute_message