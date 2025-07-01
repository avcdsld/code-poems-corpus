def close_job(self, job_id):
        """
        Closes job

        :param job_id: job_id as returned by 'create_operation_job(...)'
        :return: close response as xml
        """
        if not job_id or not self.has_active_session():
            raise Exception("Can not close job without valid job_id and an active session.")

        response = requests.post(self._get_close_job_url(job_id),
                                 headers=self._get_close_job_headers(),
                                 data=self._get_close_job_xml())
        response.raise_for_status()

        return response