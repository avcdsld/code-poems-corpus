def delete_log(
        self,
        log_name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes all the log entries in a log.
        The log reappears if it receives new entries.
        Log entries written shortly before the delete operation might not be
        deleted.

        Example:
            >>> from google.cloud import logging_v2
            >>>
            >>> client = logging_v2.LoggingServiceV2Client()
            >>>
            >>> log_name = client.log_path('[PROJECT]', '[LOG]')
            >>>
            >>> client.delete_log(log_name)

        Args:
            log_name (str): Required. The resource name of the log to delete:

                ::

                     "projects/[PROJECT_ID]/logs/[LOG_ID]"
                     "organizations/[ORGANIZATION_ID]/logs/[LOG_ID]"
                     "billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]"
                     "folders/[FOLDER_ID]/logs/[LOG_ID]"

                ``[LOG_ID]`` must be URL-encoded. For example,
                ``"projects/my-project-id/logs/syslog"``,
                ``"organizations/1234567890/logs/cloudresourcemanager.googleapis.com%2Factivity"``.
                For more information about log names, see ``LogEntry``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_log" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_log"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_log,
                default_retry=self._method_configs["DeleteLog"].retry,
                default_timeout=self._method_configs["DeleteLog"].timeout,
                client_info=self._client_info,
            )

        request = logging_pb2.DeleteLogRequest(log_name=log_name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("log_name", log_name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_log"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )