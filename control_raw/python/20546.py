def get_batch_result_ids(self, job_id, batch_id):
        """
        Get result IDs of a batch that has completed processing.

        :param job_id: job_id as returned by 'create_operation_job(...)'
        :param batch_id: batch_id as returned by 'create_batch(...)'
        :return: list of batch result IDs to be used in 'get_batch_result(...)'
        """
        response = requests.get(self._get_batch_results_url(job_id, batch_id),
                                headers=self._get_batch_info_headers())
        response.raise_for_status()

        root = ET.fromstring(response.text)
        result_ids = [r.text for r in root.findall('%sresult' % self.API_NS)]

        return result_ids