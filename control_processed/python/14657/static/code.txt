def create_dlp_job(
        self,
        parent,
        inspect_job=None,
        risk_job=None,
        job_id=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new job to inspect storage or calculate risk metrics.
        See https://cloud.google.com/dlp/docs/inspecting-storage and
        https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more.

        When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the
        system will automatically choose what detectors to run. By default this may
        be all types, but may change over time as detectors are updated.

        Example:
            >>> from google.cloud import dlp_v2
            >>>
            >>> client = dlp_v2.DlpServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> response = client.create_dlp_job(parent)

        Args:
            parent (str): The parent resource name, for example projects/my-project-id.
            inspect_job (Union[dict, ~google.cloud.dlp_v2.types.InspectJobConfig]):
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dlp_v2.types.InspectJobConfig`
            risk_job (Union[dict, ~google.cloud.dlp_v2.types.RiskAnalysisJobConfig]):
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dlp_v2.types.RiskAnalysisJobConfig`
            job_id (str): The job id can contain uppercase and lowercase letters, numbers, and
                hyphens; that is, it must match the regular expression:
                ``[a-zA-Z\\d-_]+``. The maximum length is 100 characters. Can be empty
                to allow the system to generate one.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dlp_v2.types.DlpJob` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_dlp_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_dlp_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_dlp_job,
                default_retry=self._method_configs["CreateDlpJob"].retry,
                default_timeout=self._method_configs["CreateDlpJob"].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            inspect_job=inspect_job, risk_job=risk_job
        )

        request = dlp_pb2.CreateDlpJobRequest(
            parent=parent, inspect_job=inspect_job, risk_job=risk_job, job_id=job_id
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_dlp_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )