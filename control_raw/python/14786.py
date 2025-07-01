def create_table(
        self,
        parent,
        table_id,
        table,
        initial_splits=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new table in the specified instance.
        The table can be created with a full set of initial column families,
        specified in the request.

        Example:
            >>> from google.cloud import bigtable_admin_v2
            >>>
            >>> client = bigtable_admin_v2.BigtableTableAdminClient()
            >>>
            >>> parent = client.instance_path('[PROJECT]', '[INSTANCE]')
            >>>
            >>> # TODO: Initialize `table_id`:
            >>> table_id = ''
            >>>
            >>> # TODO: Initialize `table`:
            >>> table = {}
            >>>
            >>> response = client.create_table(parent, table_id, table)

        Args:
            parent (str): The unique name of the instance in which to create the table. Values are
                of the form ``projects/<project>/instances/<instance>``.
            table_id (str): The name by which the new table should be referred to within the parent
                instance, e.g., ``foobar`` rather than ``<parent>/tables/foobar``.
            table (Union[dict, ~google.cloud.bigtable_admin_v2.types.Table]): The Table to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigtable_admin_v2.types.Table`
            initial_splits (list[Union[dict, ~google.cloud.bigtable_admin_v2.types.Split]]): The optional list of row keys that will be used to initially split the
                table into several tablets (tablets are similar to HBase regions). Given
                two split keys, ``s1`` and ``s2``, three tablets will be created,
                spanning the key ranges: ``[, s1), [s1, s2), [s2, )``.

                Example:

                -  Row keys := ``["a", "apple", "custom", "customer_1", "customer_2",``
                   ``"other", "zz"]``
                -  initial\_split\_keys :=
                   ``["apple", "customer_1", "customer_2", "other"]``
                -  Key assignment:

                   -  Tablet 1 ``[, apple)                => {"a"}.``
                   -  Tablet 2 ``[apple, customer_1)      => {"apple", "custom"}.``
                   -  Tablet 3 ``[customer_1, customer_2) => {"customer_1"}.``
                   -  Tablet 4 ``[customer_2, other)      => {"customer_2"}.``
                   -  Tablet 5 ``[other, )                => {"other", "zz"}.``

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigtable_admin_v2.types.Split`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigtable_admin_v2.types.Table` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_table" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_table"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_table,
                default_retry=self._method_configs["CreateTable"].retry,
                default_timeout=self._method_configs["CreateTable"].timeout,
                client_info=self._client_info,
            )

        request = bigtable_table_admin_pb2.CreateTableRequest(
            parent=parent, table_id=table_id, table=table, initial_splits=initial_splits
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

        return self._inner_api_calls["create_table"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )