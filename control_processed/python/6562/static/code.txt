def get_work_result(self, function_arn, invocation_id):
        """
        Retrieve the result of the work processed by :code:`function_arn`
        with specified :code:`invocation_id`.

        :param function_arn: Arn of the Lambda function intended to receive the work for processing.
        :type function_arn: string

        :param invocation_id: Invocation ID of the work that is being requested
        :type invocation_id: string

        :returns: The get work result output contains result payload and function error type if the invoking is failed.
        :type returns: GetWorkResultOutput
        """
        url = self._get_url(function_arn)

        runtime_logger.info('Getting work result for invocation id [{}] from {}'.format(invocation_id, url))

        request = Request(url)
        request.add_header(HEADER_INVOCATION_ID, invocation_id)
        request.add_header(HEADER_AUTH_TOKEN, self.auth_token)

        response = urlopen(request)

        runtime_logger.info('Got result for invocation id [{}]'.format(invocation_id))

        payload = response.read()
        func_err = response.info().get(HEADER_FUNCTION_ERR_TYPE)

        return GetWorkResultOutput(
            payload=payload,
            func_err=func_err)