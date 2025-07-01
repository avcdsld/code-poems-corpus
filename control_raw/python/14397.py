def list_events(
        self,
        project_name,
        group_id,
        service_filter=None,
        time_range=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists the specified events.

        Example:
            >>> from google.cloud import errorreporting_v1beta1
            >>>
            >>> client = errorreporting_v1beta1.ErrorStatsServiceClient()
            >>>
            >>> project_name = client.project_path('[PROJECT]')
            >>>
            >>> # TODO: Initialize `group_id`:
            >>> group_id = ''
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_events(project_name, group_id):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_events(project_name, group_id).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            project_name (str): [Required] The resource name of the Google Cloud Platform project.
                Written as ``projects/`` plus the `Google Cloud Platform project
                ID <https://support.google.com/cloud/answer/6158840>`__. Example:
                ``projects/my-project-123``.
            group_id (str): [Required] The group for which events shall be returned.
            service_filter (Union[dict, ~google.cloud.errorreporting_v1beta1.types.ServiceContextFilter]): [Optional] List only ErrorGroups which belong to a service context that
                matches the filter. Data for all service contexts is returned if this
                field is not specified.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.errorreporting_v1beta1.types.ServiceContextFilter`
            time_range (Union[dict, ~google.cloud.errorreporting_v1beta1.types.QueryTimeRange]): [Optional] List only data for the given time range. If not set a default
                time range is used. The field time\_range\_begin in the response will
                specify the beginning of this time range.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.errorreporting_v1beta1.types.QueryTimeRange`
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.gax.PageIterator` instance. By default, this
            is an iterable of :class:`~google.cloud.errorreporting_v1beta1.types.ErrorEvent` instances.
            This object can also be configured to iterate over the pages
            of the response through the `options` parameter.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_events" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_events"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_events,
                default_retry=self._method_configs["ListEvents"].retry,
                default_timeout=self._method_configs["ListEvents"].timeout,
                client_info=self._client_info,
            )

        request = error_stats_service_pb2.ListEventsRequest(
            project_name=project_name,
            group_id=group_id,
            service_filter=service_filter,
            time_range=time_range,
            page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("project_name", project_name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_events"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="error_events",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator