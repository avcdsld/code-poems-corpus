def total_bytes_processed(self):
        """Return total bytes processed from job statistics, if present.

        See:
        https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs#statistics.query.totalBytesProcessed

        :rtype: int or None
        :returns: total bytes processed by the job, or None if job is not
                  yet complete.
        """
        result = self._job_statistics().get("totalBytesProcessed")
        if result is not None:
            result = int(result)
        return result