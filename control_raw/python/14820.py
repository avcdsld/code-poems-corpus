def run_query(
        self,
        project_id,
        partition_id,
        read_options=None,
        query=None,
        gql_query=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Queries for entities.

        Example:
            >>> from google.cloud import datastore_v1
            >>>
            >>> client = datastore_v1.DatastoreClient()
            >>>
            >>> # TODO: Initialize `project_id`:
            >>> project_id = ''
            >>>
            >>> # TODO: Initialize `partition_id`:
            >>> partition_id = {}
            >>>
            >>> response = client.run_query(project_id, partition_id)

        Args:
            project_id (str): The ID of the project against which to make the request.
            partition_id (Union[dict, ~google.cloud.datastore_v1.types.PartitionId]): Entities are partitioned into subsets, identified by a partition ID.
                Queries are scoped to a single partition.
                This partition ID is normalized with the standard default context
                partition ID.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datastore_v1.types.PartitionId`
            read_options (Union[dict, ~google.cloud.datastore_v1.types.ReadOptions]): The options for this query.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datastore_v1.types.ReadOptions`
            query (Union[dict, ~google.cloud.datastore_v1.types.Query]): The query to run.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datastore_v1.types.Query`
            gql_query (Union[dict, ~google.cloud.datastore_v1.types.GqlQuery]): The GQL query to run.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datastore_v1.types.GqlQuery`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datastore_v1.types.RunQueryResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "run_query" not in self._inner_api_calls:
            self._inner_api_calls[
                "run_query"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.run_query,
                default_retry=self._method_configs["RunQuery"].retry,
                default_timeout=self._method_configs["RunQuery"].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(query=query, gql_query=gql_query)

        request = datastore_pb2.RunQueryRequest(
            project_id=project_id,
            partition_id=partition_id,
            read_options=read_options,
            query=query,
            gql_query=gql_query,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("project_id", project_id)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["run_query"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )