def create_instruction(
        self,
        parent,
        instruction,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates an instruction for how data should be labeled.

        Example:
            >>> from google.cloud import datalabeling_v1beta1
            >>>
            >>> client = datalabeling_v1beta1.DataLabelingServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # TODO: Initialize `instruction`:
            >>> instruction = {}
            >>>
            >>> response = client.create_instruction(parent, instruction)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): Required. Instruction resource parent, format: projects/{project\_id}
            instruction (Union[dict, ~google.cloud.datalabeling_v1beta1.types.Instruction]): Required. Instruction of how to perform the labeling task.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.datalabeling_v1beta1.types.Instruction`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.datalabeling_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_instruction" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_instruction"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_instruction,
                default_retry=self._method_configs["CreateInstruction"].retry,
                default_timeout=self._method_configs["CreateInstruction"].timeout,
                client_info=self._client_info,
            )

        request = data_labeling_service_pb2.CreateInstructionRequest(
            parent=parent, instruction=instruction
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

        operation = self._inner_api_calls["create_instruction"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            instruction_pb2.Instruction,
            metadata_type=proto_operations_pb2.CreateInstructionMetadata,
        )