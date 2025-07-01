def delete_job(self, job_id, params=None):
        """
        `<http://www.elastic.co/guide/en/elasticsearch/reference/current/ml-delete-job.html>`_

        :arg job_id: The ID of the job to delete
        :arg force: True if the job should be forcefully deleted, default False
        :arg wait_for_completion: Should this request wait until the operation
            has completed before returning, default True
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'job_id'.")
        return self.transport.perform_request(
            "DELETE", _make_path("_ml", "anomaly_detectors", job_id), params=params
        )