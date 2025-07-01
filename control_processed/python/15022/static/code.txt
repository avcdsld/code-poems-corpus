def execute_batch_dml(
        self,
        session,
        transaction,
        statements,
        seqno,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Executes a batch of SQL DML statements. This method allows many
        statements to be run with lower latency than submitting them
        sequentially with ``ExecuteSql``.

        Statements are executed in order, sequentially.
        ``ExecuteBatchDmlResponse`` will contain a ``ResultSet`` for each DML
        statement that has successfully executed. If a statement fails, its
        error status will be returned as part of the
        ``ExecuteBatchDmlResponse``. Execution will stop at the first failed
        statement; the remaining statements will not run.

        ExecuteBatchDml is expected to return an OK status with a response even
        if there was an error while processing one of the DML statements.
        Clients must inspect response.status to determine if there were any
        errors while processing the request.

        See more details in ``ExecuteBatchDmlRequest`` and
        ``ExecuteBatchDmlResponse``.

        Example:
            >>> from google.cloud import spanner_v1
            >>>
            >>> client = spanner_v1.SpannerClient()
            >>>
            >>> session = client.session_path('[PROJECT]', '[INSTANCE]', '[DATABASE]', '[SESSION]')
            >>>
            >>> # TODO: Initialize `transaction`:
            >>> transaction = {}
            >>>
            >>> # TODO: Initialize `statements`:
            >>> statements = []
            >>>
            >>> # TODO: Initialize `seqno`:
            >>> seqno = 0
            >>>
            >>> response = client.execute_batch_dml(session, transaction, statements, seqno)

        Args:
            session (str): Required. The session in which the DML statements should be performed.
            transaction (Union[dict, ~google.cloud.spanner_v1.types.TransactionSelector]): The transaction to use. A ReadWrite transaction is required. Single-use
                transactions are not supported (to avoid replay).  The caller must either
                supply an existing transaction ID or begin a new transaction.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.spanner_v1.types.TransactionSelector`
            statements (list[Union[dict, ~google.cloud.spanner_v1.types.Statement]]): The list of statements to execute in this batch. Statements are executed
                serially, such that the effects of statement i are visible to statement
                i+1. Each statement must be a DML statement. Execution will stop at the
                first failed statement; the remaining statements will not run.

                REQUIRES: statements\_size() > 0.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.spanner_v1.types.Statement`
            seqno (long): A per-transaction sequence number used to identify this request. This is
                used in the same space as the seqno in ``ExecuteSqlRequest``. See more
                details in ``ExecuteSqlRequest``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.spanner_v1.types.ExecuteBatchDmlResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "execute_batch_dml" not in self._inner_api_calls:
            self._inner_api_calls[
                "execute_batch_dml"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.execute_batch_dml,
                default_retry=self._method_configs["ExecuteBatchDml"].retry,
                default_timeout=self._method_configs["ExecuteBatchDml"].timeout,
                client_info=self._client_info,
            )

        request = spanner_pb2.ExecuteBatchDmlRequest(
            session=session, transaction=transaction, statements=statements, seqno=seqno
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("session", session)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["execute_batch_dml"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )