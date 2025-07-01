def put_calendar_job(self, calendar_id, job_id, params=None):
        """
        `<>`_

        :arg calendar_id: The ID of the calendar to modify
        :arg job_id: The ID of the job to add to the calendar
        """
        for param in (calendar_id, job_id):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")
        return self.transport.perform_request(
            "PUT",
            _make_path("_ml", "calendars", calendar_id, "jobs", job_id),
            params=params,
        )